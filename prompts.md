# LLM Prompts and Responses

## Iteration 1

### System Prompt

You will be provided with an email or email letterhead. Parse it and construct the sender's signature in JSON format.

For example:
'''
    User prompt:

    Jane Doe
    Sales & Marketing Director
    ABC Company
    3373 Gregory Lane, 40601 Frankdort
    (800) 555-1133
    jane.doe@example.com
    www.example.com

    Your response:

    {
        "__sig__": {
        "name": "Jane Doe",
        "title": "Sales & Marketing Director",
        "company": "ABC Company",
        "address": "3373 Gregory Lane, 40601 Frankdort",
        "phone": "(800) 555-1133",
        "email": "jane.doe@example.com",
        "website": "www.example.com"
        }
    }
'''

### User Prompt

aqwasa sadas

#### LLaMA-3.1 Chat (8B) Response

It seems like you provided some random characters instead of an email or email letterhead. Could you please provide the actual email or email letterhead you'd like me to parse? I'll be happy to help you construct the sender's signature in JSON format.

#### GPT-3.5 Turbo Response

```json
{
    "__sig__": {
        "name": "aqwasa sadas",
        "title": "",
        "company": "",
        "address": "",
        "phone": "",
        "email": "",
        "website": ""
    }
}
```

## Iteration 2

### System Prompt

You will be provided with an email or email letterhead. Parse it and construct the sender's signature in JSON format.

For example:
'''
    User prompt:

    Jane Doe
    Sales & Marketing Director
    ABC Company
    3373 Gregory Lane, 40601 Frankdort
    (800) 555-1133
    jane.doe@example.com
    www.example.com

    Your response:

    {
        "__sig__": {
        "name": "Jane Doe",
        "title": "Sales & Marketing Director",
        "company": "ABC Company",
        "address": "3373 Gregory Lane, 40601 Frankdort",
        "phone": "(800) 555-1133",
        "email": "jane.doe@example.com",
        "website": "www.example.com"
        }
    }
'''

If the content is invalid or cannot be parsed, return an empty JSON object (i.e {})

### User Prompt

aqwasa sadas

#### LLaMA-3.1 Chat (8B) Response

It seems like you didn't provide an email or email letterhead. Please provide the text, and I'll be happy to help you parse it and construct the sender's signature in JSON format.

#### GPT-3.5 Turbo Response

```json
{
    "__sig__": {
        "name": "",
        "title": "",
        "company": "",
        "address": "",
        "phone": "",
        "email": "",
        "website": ""
    }
}
```

## Iteration 3

### System Prompt

You will be provided with an email or email letterhead. Parse it and construct the sender's signature in JSON format. If the content is invalid or cannot be parsed, return an empty JSON object (i.e {})

For example:
'''
Case 1
======

    User prompt:

    Jane Doe
    Sales & Marketing Director
    ABC Company
    3373 Gregory Lane, 40601 Frankdort
    (800) 555-1133
    jane.doe@example.com
    www.example.com

    Your response:

    {
        "__sig__": {
        "name": "Jane Doe",
        "title": "Sales & Marketing Director",
        "company": "ABC Company",
        "address": "3373 Gregory Lane, 40601 Frankdort",
        "phone": "(800) 555-1133",
        "email": "jane.doe@example.com",
        "website": "www.example.com"
        }
    }

Case 2
======

    User prompt:

    wasasak sahsaj

    Your response:

    {}
'''

### User Prompt 1

aqwasa sadas

#### LLaMA-3.1 Chat (8B) Response

{}

The input is not a valid email or email letterhead, so I couldn't parse it to construct a signature in JSON format.

#### GPT-3.5 Turbo Response

```json
{}
```

### User Prompt 2

Let's see what's Rumbling...

Summer is the season for spending quality time with grill-friends, getting some Vitamin ‘sea’, and staying cool with trending videos on Rumble. Catch up on shocking headlines and travel news, plus Rumble Studio, a game-changer for the creator economy, and ad-free videos with Rumble Premium.

Joe Blow
Head of Sales
Rumble LLC
3373 Gregory Lane, 40601 Frankdort
(800) 555-1133
<joe.blow@romnle.net>
<www.rumble.net>

#### LLaMA-3.1 Chat (8B) Response

Here is the parsed sender's signature in JSON format:

```
{
  "__sig__": {
    "name": "Joe Blow",
    "title": "Head of Sales",
    "company": "Rumble LLC",
    "address": "3373 Gregory Lane, 40601 Frankdort",
    "phone": "(800) 555-1133",
    "email": "joe.blow@romnle.net",
    "website": "www.rumble.net"
  }
}
```

#### GPT-3.5 Turbo Response

```json
{
    "__sig__": {
        "name": "Joe Blow",
        "title": "Head of Sales",
        "company": "Rumble LLC",
        "address": "3373 Gregory Lane, 40601 Frankdort",
        "phone": "(800) 555-1133",
        "email": "<joe.blow@romnle.net>",
        "website": "www.rumble.net"
    }
}
```
