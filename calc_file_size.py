def calc_file_size(num_API_requests):
    json_file_size_kb = 154/10 # got from test of 100 sample results, stored as a JSON
    pause = 0.5
    # batch_size = 250
    mb_filesize = (num_API_requests*json_file_size_kb)/1000
    
    if mb_filesize < 100:
        judgement = "managable."
    else:
        judgement = "getting chunky."

    print(f"For {num_API_requests} JSON objects, it will take {round(num_API_requests*pause/60,2)} mins to fetch and at {json_file_size_kb} KB per object, total filesize will be {mb_filesize} MB; that's {judgement}")

# calc_file_size(400)