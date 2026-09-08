# Politiques à coller dans Shopify — Settings › Policies (v2, 08/09/2026)

Le connecteur n'a pas le droit `write_legal_policies` : coller chaque bloc HTML dans Paramètres › Politiques (Shipping, Returns & refunds, Privacy, Terms of service, Contact information). Le pied de page pointe déjà vers `/policies/*`.

**Base légale UK vérifiée le 08/09/2026** : Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 (infos précontractuelles Schedule 2, annulation 14 j, formulaire modèle Schedule 3, remboursement sous 14 j), Consumer Rights Act 2015 (conformité, droit de rejet 30 j, réparation/remplacement, présomption 6 mois), Electronic Commerce (EC Directive) Regulations 2002 (identité, adresse géographique, e-mail, registre, n° TVA), UK GDPR + Data Protection Act 2018 + PECR (cookies, e-mails), ADR Regulations 2015 (dire si on recourt ou non à un médiateur), règles TVA HMRC pour les envois ≤ 135 £ vendus par un vendeur étranger.

## Placeholders à remplir par Hakim avant de coller

| Placeholder | Où | Note |
|---|---|---|
| `[UK VAT NUMBER]` | Terms, Contact | **Point bloquant** : un vendeur hors UK qui expédie des colis ≤ 135 £ à des particuliers britanniques doit être immatriculé à la TVA au Royaume-Uni et facturer la TVA à la vente (guidance HMRC « VAT and overseas goods sold directly to customers in the UK »). Le prix 89 £ est sous ce seuil. À voir avec l'expert-comptable : immatriculation TVA UK d'OH Ventures, ou autre montage. Sans numéro, retirer la ligne mais le risque reste. |
| `[FR VAT NUMBER]` | Contact | N° de TVA intracommunautaire d'OH Ventures (FR + 11 caractères). |
| `[PHONE]` | Contact, Terms | Ligne vocale réellement décrochée (checklist Terry : SIM > VoIP). Sinon retirer la ligne partout, y compris le pied de page. |
| `[RCS]` | Contact | « RCS Paris 103 157 251 » si c'est bien le greffe de Paris. |

Chiffres à garder identiques partout (policies, FAQ, fiche, pied de page, réglages Google) : traitement 1–2 jours ouvrés, transit 5–8 jours ouvrés, total **6–10 jours ouvrés** ; annulation 14 j légale + **30 j** commerciale ; remboursement sous **14 jours** après réception du retour ; réponse support sous **1 jour ouvré**. Moyens de paiement réellement actifs au checkout le 08/09 : cartes (Visa, Mastercard, American Express, Maestro), PayPal, Apple Pay, Shop Pay. **Google Pay n'est pas actif** (`/payments/config`) : l'icône du pied de page vient des réglages Shopify Payments, à activer ou à retirer pour éviter le décalage.


## 1. Shipping policy

```html
<h2>Shipping policy</h2>
<p>This policy applies to every order placed on cosycathouse.com. The shop is run by OH Ventures (SASU), a French company, and delivers to the United Kingdom only.</p>

<h3>Where we deliver</h3>
<p>England, Scotland, Wales and Northern Ireland. We don't currently deliver to the Channel Islands, the Isle of Man, BFPO addresses or outside the UK.</p>

<h3>Delivery cost</h3>
<p>Delivery is free on every order. There is no minimum spend and no hidden handling fee. The price you see on the product page is the total price, VAT included.</p>

<h3>How long it takes</h3>
<table>
<tr><th>Step</th><th>Time</th></tr>
<tr><td>Order cut-off</td><td>Orders placed before 11:59 pm (UK time) count as received that day. Orders placed on a weekend or bank holiday are processed on the next working day.</td></tr>
<tr><td>Processing</td><td>1–2 working days</td></tr>
<tr><td>Transit</td><td>5–8 working days</td></tr>
<tr><td>Total estimated delivery</td><td><strong>6–10 working days</strong> from the day your order is confirmed</td></tr>
</table>
<p>Your shelter ships directly from our supplier's warehouse rather than from a UK depot. That is why delivery is slower than next-day, and why we can keep it free. The times above are estimates based on the deliveries we actually see; they are not a guaranteed date. In any case, and as UK law requires, we will deliver within 30 days of your order unless you agree otherwise. If we cannot, you can cancel and receive a full refund.</p>

<h3>Carriers and tracking</h3>
<p>Parcels travel with the courier network used by our supplier for the UK (typically an international carrier for the first leg, then Royal Mail or Evri for the final delivery). You receive an order confirmation e-mail straight away, then a dispatch e-mail with a tracking number as soon as the parcel leaves the warehouse. You can follow it on our <a href="/apps/parcelpanel">Track order</a> page.</p>

<h3>Customs, duties and VAT</h3>
<p>Prices include UK VAT. You will not be asked to pay any customs duty, import VAT or handling charge on delivery: if a courier ever asks you for one, contact us before paying and we will sort it out.</p>

<h3>Delivery problems</h3>
<ul>
<li><strong>Late parcel</strong> — if your order hasn't arrived within 10 working days, e-mail us at <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> with your order number. We open an enquiry with the carrier and, if the parcel is lost, we send a replacement or refund you in full.</li>
<li><strong>Damaged parcel</strong> — please photograph the packaging and the item before opening it fully, and contact us within 48 hours. Damaged goods are replaced or refunded at our cost.</li>
<li><strong>Wrong address</strong> — check your address carefully at checkout. If you spot a mistake, e-mail us immediately: we can correct it until the order is dispatched.</li>
</ul>
<p>The shelter becomes your responsibility (the risk passes to you) only once it has been delivered to you or to someone you have nominated to receive it.</p>

<h3>Contact</h3>
<p>Cosy Cat House — OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, France · <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> · We reply within one working day, Monday to Friday.</p>
```


## 2. Returns & refunds policy

```html
<h2>Returns &amp; refunds policy</h2>
<p>Two sets of rules protect you when you buy from Cosy Cat House: your legal rights as a UK consumer, and our own 30-day return window on top of them. Nothing in this policy reduces your statutory rights.</p>

<h3>1. Your legal right to cancel — 14 days</h3>
<p>Under the Consumer Contracts Regulations 2013 you can cancel your order for any reason, without giving a reason, at any time from the moment you place it until <strong>14 days after the day you (or someone you nominate) receive the shelter</strong>.</p>
<p>To cancel, tell us clearly before the 14 days run out: e-mail <a href="mailto:info@ohventures.fr">info@ohventures.fr</a>, or use the model cancellation form at the end of this policy. Cancelling on the last day is enough, even if we read your message later.</p>
<p>You then have a further <strong>14 days</strong> from the day you tell us to send the shelter back. You pay the cost of returning it (see section 5); we refund the price you paid, including our standard delivery cost, which is free.</p>

<h3>2. Our 30-day return window</h3>
<p>On top of your legal right, we accept returns for <strong>30 days from delivery</strong> if the shelter isn't right for you or your cat — wrong spot, wrong size, or a cat that won't settle into it even after trying our adoption guide. The same conditions as below apply.</p>

<h3>3. Condition of returned items</h3>
<p>You may unpack the shelter, open it out and inspect it as you would in a shop. If you go further than that — a cat has used it, it is soiled, scratched or shows wear — we can, as the law allows, reduce your refund to reflect the loss in value, and in serious cases decline the return. Please send it back clean, folded, with its legs and packaging. There is no restocking fee.</p>

<h3>4. How to return</h3>
<ol>
<li>E-mail <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> with your order number and, if you like, a word about why.</li>
<li>We reply within one working day with the return address (OH Ventures, 47 rue Vivienne, 75002 Paris, France, unless we give you a closer address) and a return reference.</li>
<li>Post the parcel with a tracked service and keep the proof of postage: it is your evidence if the parcel goes missing. We cannot accept returns in person.</li>
<li>Send us the tracking number. We refund you once the parcel arrives and has been checked.</li>
</ol>

<h3>5. Who pays return postage</h3>
<ul>
<li><strong>Change of mind</strong> (legal cancellation or our 30-day window): you pay the return postage. We do not provide a prepaid label.</li>
<li><strong>Faulty, damaged or not as described</strong>: we pay. Tell us first and we will either send a prepaid label or refund your postage on proof of cost.</li>
</ul>

<h3>6. Refunds</h3>
<p>Refunds go back to the payment method you used, within <strong>14 days</strong> of the day we receive the shelter back (or of the day you give us proof of posting it, if that comes first). We do not charge any fee. Your bank or card issuer may take a few extra days to show the money.</p>

<h3>7. Faulty or misdescribed goods — Consumer Rights Act 2015</h3>
<p>The shelter must match its description, be of satisfactory quality and fit for purpose. If it isn't:</p>
<ul>
<li>within <strong>30 days</strong> of delivery you can reject it and receive a full refund;</li>
<li>after that, and up to six years, you are entitled to a repair or replacement; if that fails or can't be done in reasonable time, to a price reduction or a refund (which may be reduced for use after the first six months);</li>
<li>during the first <strong>six months</strong> a fault is presumed to have been there at delivery unless we prove otherwise.</li>
</ul>
<p>Contact us with photos and your order number within 48 hours of noticing the problem where possible. We cover return costs and replace or refund at your choice within what the law allows.</p>

<h3>8. Cancelling before dispatch</h3>
<p>If your order hasn't been dispatched yet, e-mail us and we cancel it and refund you straight away. Once it has left the warehouse, please follow the return steps above.</p>

<h3>9. Exchanges</h3>
<p>We don't run exchanges: return the shelter for a refund and place a new order. It is faster and guarantees availability.</p>

<h3>Model cancellation form</h3>
<p>Copy this into an e-mail to <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> if you wish to cancel (you don't have to use it):</p>
<p><em>To OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, France — info@ohventures.fr<br>
I/We [*] hereby give notice that I/We [*] cancel my/our [*] contract of sale of the following goods: [description], ordered on [date] / received on [date].<br>
Name of consumer(s): … Address of consumer(s): … Signature (only if this form is notified on paper): … Date: …<br>
[*] Delete as appropriate.</em></p>

<h3>Contact</h3>
<p>Cosy Cat House — OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, France · <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> · We reply within one working day, Monday to Friday.</p>
```


## 3. Privacy policy

```html
<h2>Privacy policy</h2>
<p>This notice explains what personal data Cosy Cat House collects when you visit cosycathouse.com or place an order, why, and what your rights are. It is written to comply with the UK General Data Protection Regulation (UK GDPR), the Data Protection Act 2018 and the Privacy and Electronic Communications Regulations (PECR), as well as the EU GDPR that applies to us as a French company.</p>

<h3>1. Who is responsible for your data</h3>
<p>The data controller is <strong>OH Ventures (SASU)</strong>, 47 rue Vivienne, 75002 Paris, France, registered under SIREN 103 157 251, trading as Cosy Cat House. Contact for anything about your data: <a href="mailto:info@ohventures.fr">info@ohventures.fr</a>. We are established in the European Union and do not have an office in the UK; our processing of UK customers' data is occasional and limited to running this shop, so we have not appointed a UK representative under Article 27 UK GDPR. You can contact us directly at the address above.</p>

<h3>2. What we collect</h3>
<ul>
<li><strong>Identity and contact</strong>: name, e-mail address, phone number if you give it.</li>
<li><strong>Delivery and billing</strong>: postal address.</li>
<li><strong>Order data</strong>: what you bought, when, for how much, and our correspondence with you.</li>
<li><strong>Payment data</strong>: handled by Shopify Payments, PayPal, Apple Pay or Shop Pay. We never see or store your full card number.</li>
<li><strong>Technical data</strong>: IP address, device and browser type, pages viewed, referring site, collected through cookies and similar technologies (see section 7).</li>
</ul>
<p>We do not collect special-category data and we do not knowingly collect data from children under 16.</p>

<h3>3. Why we use it, and on what legal basis</h3>
<table>
<tr><th>Purpose</th><th>Legal basis (UK GDPR Article 6)</th></tr>
<tr><td>Taking, delivering and supporting your order; returns and refunds</td><td>Performance of a contract</td></tr>
<tr><td>Keeping accounting and tax records</td><td>Legal obligation</td></tr>
<tr><td>Preventing fraud and securing the site</td><td>Legitimate interests</td></tr>
<tr><td>Order and delivery e-mails</td><td>Performance of a contract</td></tr>
<tr><td>Marketing e-mails about our products</td><td>Consent, or the PECR "soft opt-in" for existing customers — every e-mail has an unsubscribe link</td></tr>
<tr><td>Site analytics and advertising measurement</td><td>Consent, given through the cookie banner</td></tr>
</table>
<p>We do not make automated decisions with legal effects about you, and we do not sell your data.</p>

<h3>4. Who receives your data</h3>
<p>Only providers we need to run the shop, each bound by a data-processing agreement: <strong>Shopify</strong> (store platform, checkout, payments — Shopify International Ltd, Ireland, and Shopify Inc., Canada), <strong>PayPal</strong> and the card networks for payments, <strong>DSers</strong> and our supplier's logistics partner for order fulfilment (they receive your name, address and phone number to deliver the parcel), the <strong>carriers</strong> (Royal Mail, Evri or equivalent), <strong>ParcelPanel</strong> for order tracking, <strong>Google</strong> for analytics and advertising measurement when you accept those cookies, and our e-mail provider. Public authorities may receive data where the law requires it.</p>

<h3>5. International transfers</h3>
<p>We are in France. Your data therefore leaves the UK for the European Economic Area, which the UK government has found to provide adequate protection. Some providers (Shopify, Google, our supplier's logistics partner) process data outside the UK and the EEA, notably in Canada, the United States and China. Those transfers rely on UK adequacy regulations where they exist (Canada) and otherwise on the UK International Data Transfer Agreement or the UK Addendum to the EU Standard Contractual Clauses, with additional safeguards. You can ask us for details.</p>

<h3>6. How long we keep it</h3>
<ul>
<li>Order, invoice and correspondence data: <strong>10 years</strong> after the order, as French accounting law requires.</li>
<li>Customer account data: until you close the account, then deleted within 3 years of your last order.</li>
<li>Marketing consent: until you withdraw it; contact lists are reviewed every 3 years.</li>
<li>Technical logs and cookie data: 13 months at most.</li>
</ul>

<h3>7. Cookies</h3>
<p>Essential cookies (basket, checkout, security) are always on. Analytics and advertising cookies (Shopify analytics, Google Analytics, Google Ads conversion tracking) are set only if you accept them in the banner shown on your first visit. You can change your choice at any time in your browser settings; deleting our cookies makes the banner appear again on your next visit. Refusing them doesn't affect your ability to order.</p>

<h3>8. Your rights</h3>
<p>You can ask us, free of charge, to: access the data we hold about you; correct it; erase it; restrict or object to how we use it; receive it in a portable format; and withdraw consent at any time without affecting earlier processing. Write to <a href="mailto:info@ohventures.fr">info@ohventures.fr</a>; we answer within one month. If you are unhappy with our answer you can complain to the UK Information Commissioner's Office (<a href="https://ico.org.uk" rel="nofollow">ico.org.uk</a>, helpline 0303 123 1113) or to the French CNIL (<a href="https://www.cnil.fr" rel="nofollow">cnil.fr</a>).</p>

<h3>9. Security</h3>
<p>The site and checkout run over encrypted connections (TLS). Access to order data is restricted to the people who need it. Payments are processed by PCI-DSS certified providers.</p>

<h3>10. Changes</h3>
<p>We update this notice when our practices change. Version dated 8 September 2026.</p>
```


## 4. Terms of service

```html
<h2>Terms of service</h2>
<p>These terms govern every purchase made on cosycathouse.com. Please read them before ordering. By placing an order you accept them; they don't affect your statutory rights as a UK consumer.</p>

<h3>1. Who you are buying from</h3>
<p>The seller is <strong>OH Ventures</strong>, a French simplified joint-stock company (SASU) with share capital, registered office at 47 rue Vivienne, 75002 Paris, France, registered with the Paris Trade and Companies Register under number 103 157 251 (SIREN), EU VAT number [FR VAT NUMBER], UK VAT number [UK VAT NUMBER], trading under the name Cosy Cat House. E-mail: <a href="mailto:info@ohventures.fr">info@ohventures.fr</a>. Telephone: [PHONE].</p>

<h3>2. The product</h3>
<p>We sell an insulated outdoor shelter for cats. We describe it as accurately as we can: dimensions, materials and features are stated on the product page. Product images are studio and lifestyle compositions of the item sold; small differences in shade or finish can occur. The shelter is an insulated, unheated shelter — it is not waterproof to the point of immersion and it does not guarantee protection against other animals. It is intended for domestic cats and should be used as described.</p>

<h3>3. Prices</h3>
<p>All prices are in pounds sterling and include UK VAT at the current rate. Delivery is free. If we discover a pricing error before dispatch, we will contact you and give you the choice of confirming the order at the correct price or cancelling it for a full refund.</p>

<h3>4. Ordering and contract formation</h3>
<p>Placing an order is an offer to buy. We send an order acknowledgement by e-mail; the contract is formed when we send the dispatch confirmation. We may refuse or cancel an order where we suspect fraud, where the product is unavailable or where a delivery address is outside the UK — in which case you are refunded in full. Your order confirmation e-mail is your durable copy of these terms and of what you ordered; keep it.</p>

<h3>5. Payment</h3>
<p>You can pay by Visa, Mastercard, American Express or Maestro card, PayPal, Apple Pay or Shop Pay. Payment is taken when you place the order. All transactions are encrypted and processed by certified payment providers; we never store your full card details.</p>

<h3>6. Delivery</h3>
<p>We deliver to UK addresses only, free of charge, within an estimated 6–10 working days (processing 1–2 working days, transit 5–8 working days). Full details, including what happens if a parcel is late or damaged, are in our <a href="/policies/shipping-policy">Shipping policy</a>. Risk in the goods passes to you on delivery; ownership passes when we receive payment in full.</p>

<h3>7. Your right to cancel and to return</h3>
<p>You have a statutory right to cancel within 14 days of receiving the goods, and we add a 30-day return window on top. Return postage for a change of mind is at your cost; faulty goods are returned at ours. The full procedure, deadlines, refund timing (within 14 days of receiving the goods back) and the model cancellation form are in our <a href="/policies/refund-policy">Returns &amp; refunds policy</a>.</p>

<h3>8. Our legal duty and your statutory rights</h3>
<p>We are under a legal duty to supply goods that conform to the contract. Under the Consumer Rights Act 2015 you are entitled to reject faulty goods within 30 days for a full refund, and thereafter to a repair or replacement, or a price reduction or refund if that fails. Nothing in these terms excludes or limits those rights, our liability for death or personal injury caused by our negligence, for fraud, or any other liability that cannot be limited by law.</p>

<h3>9. Our liability</h3>
<p>Subject to section 8, we are responsible for foreseeable loss caused by our breach of these terms or our negligence, up to the price you paid for the order. We are not liable for loss that was not foreseeable, for business losses, or for damage caused by using the shelter other than as intended.</p>

<h3>10. Complaints and disputes</h3>
<p>If something goes wrong, e-mail <a href="mailto:info@ohventures.fr">info@ohventures.fr</a> with your order number: we acknowledge within one working day and aim to resolve every complaint within 14 days. We are not a member of an alternative dispute resolution (ADR) scheme and have not committed to using one; if we cannot resolve a dispute together, you may take it to the courts (see section 12). UK consumers can also seek free advice from Citizens Advice.</p>

<h3>11. Intellectual property</h3>
<p>The Cosy Cat House name, logo, texts and images on this site belong to OH Ventures or are used under licence. You may not reproduce them without written permission.</p>

<h3>12. Governing law and jurisdiction</h3>
<p>These terms are governed by the law of England and Wales, and you can bring proceedings in the courts of England and Wales. If you live in Scotland or Northern Ireland you may also bring proceedings in the courts of your home nation. As a consumer you always benefit from the mandatory protections of the law of the country where you live.</p>

<h3>13. Changes</h3>
<p>We may update these terms; the version in force when you order applies to that order. Version dated 8 September 2026.</p>
```


## 5. Contact information (Shopify « Contact information » / legal notice)

```html
<h2>Contact and legal information</h2>
<p><strong>Trading name:</strong> Cosy Cat House<br>
<strong>Company:</strong> OH Ventures, SASU (French simplified joint-stock company)<br>
<strong>Registered office:</strong> 47 rue Vivienne, 75002 Paris, France<br>
<strong>Company registration:</strong> [RCS] — SIREN 103 157 251<br>
<strong>EU VAT number:</strong> [FR VAT NUMBER] · <strong>UK VAT number:</strong> [UK VAT NUMBER]<br>
<strong>E-mail:</strong> <a href="mailto:info@ohventures.fr">info@ohventures.fr</a><br>
<strong>Telephone:</strong> [PHONE] (Monday to Friday, 9 am – 5 pm UK time)<br>
<strong>Website host:</strong> Shopify International Ltd, 2nd Floor, Victoria Buildings, 1–2 Haddington Road, Dublin 4, D04 XN32, Ireland</p>
<p>We answer every message within one working day. Returns are sent to the address above unless we give you a different one when you open a return.</p>
```
