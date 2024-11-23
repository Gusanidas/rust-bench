base_prompt = """
You are a Rust coding assistant. You are going to be given a programming task and you should solve it using Rust.

Provide all the code necessary to solve the problem in the same code block.
The code should contain a main function.
The code should compile and run successfully.
You can use the following crates:
 - chrono
 - itertools
 - thiserror
 - serde = { version = "1.0", features = ["derive"] }
 - serde_json
 - anyhow
 - uuid = { version = "1.7", features = ["v4"] }
 - csv = "1.2"  # For parsing CSV files
 - tokio = { version = "1.0", features = ["full"] }
 - rand
 - reqwest
 - futures
 - url
"""

retry_prompt = """
It seems like there was an error in your code. Please fix the error and try again.

The original problem statement was:
{problem_statement}

The code provided was:
{code}

The error message is:
{error_message}
"""
