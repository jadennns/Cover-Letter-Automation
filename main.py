from replacer import * 
from ai import ai
import sys

if __name__ == "__main__":
 
    if len(sys.argv) < 2:
        print("Please provide a job posting URL as a command line argument.")
        sys.exit(1)

    job_url = sys.argv[1]

    print("Job Posting URL: ", job_url)
    print("-" * 50)

    content = ai(job_url)

    replace_body(
    new_body=content["body"]
    )

    replace_subject(
    new_subject=content["subject"]
    )

    replace_salutations(
    new_salutations=content["salutation"]
    )

    replace_date()