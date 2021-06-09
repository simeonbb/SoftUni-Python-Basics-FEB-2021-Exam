processor_usd_price = float(input())
video_card_usd_price = float(input())
price_1_ram = float(input())
count_RAMs = int(input())
discount = float(input())

bgn_processor_price = processor_usd_price * 1.57
bgn_video_card_price = video_card_usd_price * 1.57
bgn_ram_price = price_1_ram * 1.57
total_rams = bgn_ram_price * count_RAMs

discounted_processor = bgn_processor_price - (discount*bgn_processor_price)
discounted_video_card = bgn_video_card_price - (discount*bgn_video_card_price)

total_pc_store_price = discounted_processor + discounted_video_card + total_rams

print(f'Money needed - {total_pc_store_price:.2f} leva.')
