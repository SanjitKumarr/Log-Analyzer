from re import search
from os.path import join
from time import perf_counter


def parseFile(input_log):
    '''
    converts the input file present in tmp folder, 
    to a CSV file in outputFiles folder
    in the project directory
    '''
    with open(join('outputFiles', 'output.csv'), 'w') as of:
        with open(join('tmp', input_log), 'r') as f:
            entries = 0
            cache = []
            print('Started converting to CSV...')
            x = perf_counter()
            of.write(
                'IPAddress,UserAgent,RequestType,API,UserName,EnterpriseID,EnterpriseName,StatusCode\n')

            for line in f:
                if line != '':

                    # regex pattern as mentioned in the Assumptions file
                    pattern = search(
                        r'IP-Address=([\d.]+).*User-Agent=([\w \(\)/;,.:]+).*Request-Type=([\w]{3,7}).*API=([\w/]+).*User-Name=(\w+).*EnterpriseId=(\d+).*EnterpriseName=([\w-]+).*Status-Code=(\d{3})', line)
                    entries += 1
                    cache.append(','.join(pattern.groups())+'\n')

                    # A batch of 100,000 log entries are written at a go to improve speed
                    if entries % 100000 == 0:
                        of.writelines(cache)
                        cache.clear()

            if cache:
                # Remaining entries is written to the files
                of.writelines(cache)
                cache.clear()

            print('Conversion finished.')
            print(f"{perf_counter()-x}s for conversion to CSV")
