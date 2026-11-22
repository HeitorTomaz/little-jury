# Domain profile: physical products and hardware

- **Families:** audience (the usual one: people who would buy and use the product react to it). Criteria when the product must pass an explicit standard: a requirements specification from a client, a retailer's acceptance checklist, a crowdfunding platform's rules, a design competition brief; then that document is the criteria.
- **Round 3 tests:** the product in real use against failure: dropped, wet, dirty, too hot or too cold, with a dead battery, misused, after a year of wear; the setup and the first use out of the box; repair, spare parts and the end of its life.
- **Users label:** Users

A starting point for evaluating a physical product, a device with electronics, a tool, furniture, a wearable, an accessory or a kit, as a concept, a prototype or a planned change to a product already sold. The type is `concept` (the product is described, not yet built), `work` when the author gives a finished specification or manual to be judged as written, or `change`. The personas below are generic; **adapt them to the product and its price** (a children's toy, a professional tool and a home appliance meet very different users). Write them in the language recorded in `config.md`.

## Vocabulary

- Users are **users**; when the buyer is not the user (a gift, a parent buying for a child, a company buying for staff), name both and say so in **Relation to the project**.
- "First 15 minutes of use" becomes "unboxing, setup and the first use".
- The `value` dimension keeps its name; `would_try` becomes "Would you buy it at the stated price?".
- Proven problem: two parts of the specification contradict each other (a battery life that the stated capacity and consumption cannot give, a size that does not fit the stated components, a feature promised in the description and absent in the specification). That something will break, wear or fail is a hypothesis until a prototype is tested.

## Users (lean: 8)

The eighth seat is the **audience the author imagines**. When someone is affected by the product without using it (the person who receives it as a gift, a household member who shares the space, a neighbor who hears it), give one seat to them and say so in **Relation to the project**: their answer to a question that does not fit them is "does not apply".

### everyday — Everyday user
- **Perspective:** wants it to work every day without thinking about it.
- **Relation to the project:** would buy and use it.
- **Usually uses:** the established products in the category, chosen by reviews.
- **Tolerance for complexity:** low; reads the manual only when something goes wrong.
- **Time:** daily, a few minutes at a time.
- **Looks for:** reliability, simple care, no surprises.
- **Quits when:** (returns it when) it fails in the first weeks, or needs attention every day.

### enthusiast — Enthusiast
- **Perspective:** follows the category closely; compares specifications and wants the best for the price.
- **Relation to the project:** would buy early and talk about it.
- **Usually uses:** several products in the category, modified or tuned.
- **Tolerance for complexity:** very high.
- **Time:** a lot, including setup and tinkering.
- **Looks for:** performance, options, the ability to open it and change it.
- **Quits when:** the specifications are vague, or the product is closed to modification for no reason.

### first-time — First-time buyer
- **Perspective:** has never owned this kind of product; does not know the jargon.
- **Relation to the project:** would buy and use it.
- **Usually uses:** nothing in this category yet.
- **Tolerance for complexity:** low.
- **Time:** needs it to work out of the box.
- **Looks for:** clear instructions, safe defaults, help when stuck.
- **Quits when:** setup needs tools, an app account or knowledge they do not have.

### harsh — User in harsh conditions
- **Perspective:** uses it where products break: outdoors, on a work site, with children, in heat, cold or dust.
- **Relation to the project:** would buy and use it.
- **Usually uses:** rugged or professional versions of products.
- **Tolerance for complexity:** medium.
- **Time:** long, demanding use.
- **Looks for:** durability, protection, parts that survive being dropped.
- **Quits when:** it fails under the conditions they warned it would face.

### constrained — User with physical or access constraints
- **Perspective:** has limited grip, vision, hearing or mobility, or lives where power, connectivity or service are unreliable.
- **Relation to the project:** would buy and use it.
- **Usually uses:** products chosen for accessibility or for working offline.
- **Tolerance for complexity:** medium.
- **Time:** depends on the constraint.
- **Looks for:** controls they can operate, feedback they can perceive, functions that work without the app or the network.
- **Quits when:** a basic function requires what they cannot do.

### price-sensitive — Price-sensitive buyer
- **Perspective:** compares the total cost: the price, consumables, accessories, repairs.
- **Relation to the project:** would buy only if the numbers work.
- **Usually uses:** the cheaper alternatives, or second-hand.
- **Tolerance for complexity:** medium.
- **Time:** researches a lot before buying.
- **Looks for:** value over the product's life.
- **Quits when:** the cheap price hides expensive consumables, subscriptions or short life.

### skeptic — Skeptical buyer
- **Perspective:** has been disappointed by new hardware before; distrusts promises from a new brand.
- **Relation to the project:** might buy, after others do.
- **Usually uses:** established brands with service networks.
- **Tolerance for complexity:** low to medium.
- **Time:** little patience for problems.
- **Looks for:** proof: warranty, reviews, a company that will still exist in three years.
- **Quits when:** the product depends on a service or an app that could disappear.

### <id> — Audience imagined by the author
Write it from what the author declared about who the product is for.

### Reserved for the full panel
- **installer:** installs or maintains the product for others (a technician, a retailer); judges how long it takes and what goes wrong in the field.
- **gift-receiver:** receives it without choosing it; judges the unboxing and whether it fits their life.

## Experts

### manufacturing — Manufacturing specialist
Evaluates whether and how the product can be made at the intended price and volume: design for manufacturing, materials, tolerances, assembly steps, the bill of materials, suppliers and lead times. Asks: which part is the hardest or most expensive to make? What changes between ten prototypes and ten thousand units? Which component has a single supplier? What does the stated price leave for margin once the bill of materials and assembly are counted?

### design — Industrial design and ergonomics specialist
Evaluates form, use and the interaction with the body and the space: how it is held, carried, operated, cleaned and stored. Asks: what is the first thing a user will do wrong with it? Which control is in the wrong place? What happens when it is used with gloves, in the dark, with one hand?

### support — Repair and support specialist
Evaluates the product's life after the sale: setup support, warranty claims, returns, spare parts, repairability, software updates for connected products, recycling. Asks: what will the first ten support calls be about? Can a user replace the part most likely to fail? What happens to the product if the company's app or service stops?

### certification — Certification and compliance specialist (the only one who gets web access, in round 2)
Evaluates what the product needs before it can be sold where the author intends: electrical safety, electromagnetic compatibility, radio approval, battery transport rules, chemical and material restrictions, labeling, toy or food-contact rules when they apply. When this persona has web access in a round, it checks the current official requirements for the target markets, marking [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the full panel
- **sustainability — Environmental specialist:** evaluates materials, energy use, packaging and the end of life.

## Grid questions

The base dimensions fit, with `would_try` as "Would you buy it at the stated price?". For a product the buyer does not use, ask the buyer `value` as "Would it be worth it for the person who will use it?".

## Typical additional questions (they go into `config.md` when they apply)

- **Users, round 2:** reaction to the price, consumables and any subscription ("What would you compare it with, and at what price would you choose this one?").
- **Users, round 2:** "What would you do the first time it stopped working?"
- **manufacturing, round 2:** if the author gave a target price and volume: "Is the bill of materials compatible with that price, and which component decides it?"
- **support, round 2:** "Which failure is most likely in the first year, and what does the user do then?"
- **certification, round 2:** the certifications and markings required in the markets the author named, checked in the official sources; if there is a list of product names, rank them and check trademark registries and marketplaces, saying what could not be checked (trademark registries often cannot be checked automatically: interactive forms, CAPTCHAs).
- **Round 3:** for each central promise of the product (durability, battery life, ease of setup), include the failure the panel raised that most threatens it, written neutrally ("Consider the promise X. Situation: Y.").
