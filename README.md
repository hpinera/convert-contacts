# convert-contacts
Take an existing contact file from a Cisco 7925 wireless IP phone  and adjust the contents to the new Cisco 8821 contact file format.

This python script takes an existing 7925 contact file and converts it to the 8821 format. 

The script can take 2 parameters. An input file is required and an output file name is optional.  To run execute the following line from your shell

python3 convert-contacts.py <original-file-name.csv> <new-file-name.csv> 

If a new file name is omitted the output file will be the original file name prepended by "8821_".

A sample 7925 input file is included with the submission 7925Sample1.csv.  

The format for the 8821 file output was taken from :
https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cuipph/8821/english/Deployment/8821_wlandg.pdf  

The script maps certain fields, removes obsolete fields and re-orders them to match the expected format for the 8821.  

The Mappings are as you would expect for <First Name>,<Last Name>, <Nickname>, <Company>, <Work Number>, <Home Number>, <Mobile Number>, & <Email Address> 

The following fields are not used in the 8821 and therefore aren't mapped by this script:
UUID, Title, Middle Name, Suffix, Job Title, Business street, business city, business state, business postal code, business country, home street, home city, home state, home postal code, home country, home phone, home speeddial, business speeddial, mobile speeddial, business fax, business fax speed dial, other speed dial, Primary phone, & IM address

The following fields are new fields on the 8821 that are either calculated from some of the other fields or are left blank:
Work Primary, Home Primary, Mobile Primary, Work Favorite, home Favorite, Mobile Favorite

A next potential iteration could take all the files in a single directory and convert them all.
