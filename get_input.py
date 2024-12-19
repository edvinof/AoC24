import requests
import sys
import number2word

cookies = {
    "session_id": "53616c7465645f5f6ab01c4513d37204dbab234dc401902312b37bc4f64de680f01f0bd02a2d5c7d03fc36162480da667abd3ddfaf4459e022ba78c1a55e46f5"
}

input = requests.get(url=f'https://adventofcode.com/2024/day/{sys.argv[1]}/input', cookies=cookies)

with open(mode='w', file=f'{number2word.convert(sys.argv[1])}') as output:
    for line in input.text:
        output.write(line)


