room_type = input('Choose your room: ')
room_size = int(input('Choose your size: '))
room_available = 'Kamar'.lower()
if room_type.lower() == room_available and room_size > 12:
    print('\nBesar')
if room_type.lower() == room_available and room_size > 6:
    print('\nSedang')
if room_type.lower() == room_available and room_size <= 6:
    print('\nKecil')
