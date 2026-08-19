from replacer import * 
from ai import ai
import sys

if __name__ == "__main__":
 
    use_file_flag = "--usefile" in sys.argv

    if use_file_flag:
        print("Using preset file source from ai module...")
        content = ai(job_url="", with_file=True)
    else:
        if len(sys.argv) < 2:
            print("Please provide a job posting URL as a command line argument.")
            sys.exit(1)
        
        job_url = sys.argv[1]
        print(f"Job Posting URL: {job_url}")
        content = ai(job_url, with_file=False)
    
    print("-" * 50)

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