[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/cendelobening/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/cendelobening/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

# Fortune Cookie for an AI Agent

One funny fortune cookie line for an AI agent, written by a small pure-stdlib
Python program. The program writes a single line of at most 140 characters
to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, falling back
to `/output`).

The fortune:

> Your lucky numbers are in your error log. Play them before the next deploy retires you.

Built for the [Fortune Cookie for an AI Agent bounty](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) on make.fun.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

No dependencies beyond Python 3 itself.
