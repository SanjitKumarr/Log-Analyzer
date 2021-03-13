# Assumptions

- log file with empty line is also accpeted, but other than a new line, the below format <b>should</b> be present.
- The logs should be in the format:
  `<anything except newline>IP-Address=<IPV4 address>.*User-Agent=<letters or numbers other than '#'>.*Request-Type=<amongst GET POST DELETE PATCH UPDATE PUT>.*API=<letters, numbers, _ and ? are allowed>.*User-Name=<letters and numbers with underscore>.*EnterpriseId=<number>.*EnterpriseName=<letters, numbers and '-'>.*Status-Code=<any 3 digit number><anything except newline>`
  These values cannot contain a ','.

- On the query page, if nothing is provided it is assumed that he wants to see all the details.
- If no match was found, Only column names will be shown with no data below them.
- One field cannot have multiple values, i.e, One value per field.
