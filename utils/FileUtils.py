class FileUtils:

    def read_text_file(self, file_name):
        with open(file_name) as f:
            contents = f.readlines()
            return contents
            f.close()

    def write_text_file(self, results_file_name, results, coordinates):
        x1 = coordinates[0]
        y1 = coordinates[1]
        y2 = coordinates[3]
        x2 = coordinates[4]
        with open(results_file_name, 'w') as f:
            f.write(f'{f"Expecting Range X: {x1},{x2} Y : {y1},{y2}":{25}}')
            f.write('\n')
            f.write(f'{"Visited Coordinates":{25}} {"Results":{8}}')
            f.write('\n')
            for result in results:
                print(f'{result[0]:{25}} {result[1]:{8}}')
                f.write(f'{result[0]:{25}} {result[1]:{8}}')
                f.write('\n')
        f.close()
