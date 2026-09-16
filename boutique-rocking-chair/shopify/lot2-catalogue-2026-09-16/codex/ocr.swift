import Foundation
import Vision
import AppKit
let paths = CommandLine.arguments.dropFirst()
for p in paths {
  guard let img = NSImage(contentsOfFile: p), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("ERR\t\(p)"); continue }
  let req = VNRecognizeTextRequest()
  req.recognitionLevel = .accurate
  req.usesLanguageCorrection = false
  let h = VNImageRequestHandler(cgImage: cg, options: [:])
  try? h.perform([req])
  let txt = (req.results ?? []).compactMap { $0.topCandidates(1).first }.filter { $0.confidence > 0.5 && $0.string.count >= 3 }.map { $0.string }
  print("\(p)\t\(txt.joined(separator: " | "))")
}
