# EngDetector

Decides whether a piece of text is English without a model, a corpus or a network call: only the frequency table of English letters, a Beta distribution, and a bit of arithmetic.

## The idea

English has a very stable letter distribution (e ≈ 13%, z ≈ 0.07%). For any candidate string, count how each letter's observed frequency sits against that expected distribution, fit the result to a Beta distribution (`scipy.stats.beta`) via the error function, and score the whole text by how plausible that fit is. Text that is not English lands far outside the expected shape.

## Files

| File | Role |
|---|---|
| `EngDetecter.py` | Frequency table, per-letter scoring, text-level verdict |
| `friendlytextgen.py` | Generates readable random text, used to sanity-check the scorer |
| `test.py` | Runs the detector over sample strings |

## Running it

```bash
pip install scipy numpy
python test.py
```

## Why keep it

It is a useful measure of how much signal lives in a single frequency table: no training data, no GPU, no dependency on a language model, and the failure cases (short strings, names, code) are obvious in the output rather than hidden inside a probability.
