<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# extract all the info, including the screenshot and summarize, do not leave any info in the doc un extracted.

Here is a complete extraction and structured summary of everything in the **Options-Learning-1.docx** document. Note that the document contains **23 embedded screenshots/images** — the textual annotations around them are fully extracted below; the visual image content itself cannot be rendered as text, but all written notes accompanying them are captured.[^1]

***

## Module 1: Options Basics — Calls \& Puts

The document opens with a foundational framework for the four core options positions, mapped directly to your market view:[^1]


| Market View | Action | Type |
| :-- | :-- | :-- |
| Extremely Bullish | Buy | Call (CE) |
| Extremely Bearish | Buy | Put (PE) |
| Neutral to Bearish | Sell | Call (CE) |
| Neutral to Bullish | Sell | Put (PE) |

**Key mechanics noted:**[^1]

- **CE** = Call Option; **PE** = Put Option
- Buying options = **Paying premium** (Debit Trade)
- Selling options = **Collecting premium** (Credit Trade)
- For every option buyer, there is a seller on the other side
- You can **exit any options position at any time before expiry**

***

## Module 2: Practical INFY Example

The document uses **Infosys (INFY)** as a live case study with the following key price levels:[^1]

- **Current Price:** ₹1,713
- **Major Resistance:** ₹1,789
- **Major Support:** ₹1,664


### INFY Options Chain (February Expiry)

| Strike | Type | % Change | Premium (₹) |
| :-- | :-- | :-- | :-- |
| INFY FEB 1660 CE | Call Buy | -12.56% | ₹64.05 |
| INFY FEB 1800 PE | Put Buy | +8.42% | ₹85.00 |
| INFY FEB 1800 CE | Call Sell | -43.80% | ₹3.40 |
| INFY FEB 1660 PE | Put Sell | 0.00% | ₹6.70 |

### Four Scenario Application[^1]

1. **Extremely Bullish** → *Buy INFY FEB 1660 CE at ₹64.05* — captures major uptrend move above current price
2. **Extremely Bearish** → *Buy INFY FEB 1800 PE at ₹85.00* — captures major downtrend move
3. **Neutral to Bearish** (price won't break ₹1,789 resistance) → *Sell INFY FEB 1800 CE at ₹3.40* — collect premium
4. **Neutral to Bullish** (price won't break ₹1,664 support) → *Sell INFY FEB 1660 PE at ₹6.70* — collect premium

***

## Module 3: Intrinsic \& Extrinsic Value

This is a dedicated section on option premium decomposition:[^1]

**Option Premium = Intrinsic Value + Extrinsic Value**

- **Note:** Premium *decreases in value primarily due to the decrease in Extrinsic Value* (time decay / theta)
- The importance of understanding intrinsic vs. extrinsic value is to **select the right strike price**


### Intrinsic Value Formulas[^1]

- **Call Option Intrinsic Value** = Spot Price (Current Price) − Strike Price
- **Put Option Intrinsic Value** = Strike Price − Spot Price

*(If the result is negative, intrinsic value = 0; the option is Out-of-the-Money)*

***

## Module 4: Implied Volatility (IV)

The document notes that Implied Volatility is a key component of extrinsic value:[^1]

> *"Implied Volatility is calculated based on Earnings sessions, Acquisitions, global events, wars, and any market-manipulated events."*

IV expands option premiums before known events and collapses sharply after — a concept commonly called **IV Crush**.

***

## Module 5: Strike Selection — ATM, ITM, OTM

The document establishes a critical preference rule for sellers vs. buyers:[^1]


| Role | Preferred Strike | Reason |
| :-- | :-- | :-- |
| **Option Sellers** | ATM (At-the-Money) | Exponential time decay (theta) works in their favor |
| **Option Buyers** | ITM (In-the-Money) | Has intrinsic value, less dependent on time/IV |


***

## Module 6: Expiry Selection Strategy

The document provides a specific rule for expiry timing, framed around **NIFTY weekly expiry dates**:[^1]


| Strategy | Preferred Expiry |
| :-- | :-- |
| **Selling Options** | Shorter-term expiry → NIFTY 3rd \& NIFTY 10th |
| **Buying Options** | Longer-term expiry → NIFTY 17th \& NIFTY 24th |

This is consistent with theta decay logic — sellers benefit from rapid time decay near expiry, while buyers need more time for the directional move to play out.

***

## Behavioral Check ⚠️

Since this document is focused on **options selling strategies** (collecting premium on INFY at ₹3.40 and ₹6.70), a few critical biases to flag:

- **Herd Behavior:** Selling ATM options near earnings (Infosys reports quarterly) can result in an **IV Crush working *against* you** if you bought premium, or a violent spike if you sold it without awareness of the upcoming event calendar
- **Loss Aversion:** Option sellers face theoretically unlimited risk on naked calls — the low premium collected (₹3.40) can psychologically encourage under-sizing risk, leading to over-leverage
- **Anchoring:** Do not anchor to support/resistance levels (₹1,664 / ₹1,789) as static — these levels must be re-evaluated with each market session

***

## Document Structure Note

The document contains **23 embedded screenshots** (image1.png through image23.png) which appear to be charts, options chain screenshots, payoff diagrams, and educational slides from a trading platform or course. The written annotations extracted above represent all the text content present. The visual/image content of those screenshots cannot be rendered in text form, but every written label, note, formula, and table surrounding those images has been fully captured above.[^1]

<div align="center">⁂</div>

[^1]: Options-Learning-1.docx

