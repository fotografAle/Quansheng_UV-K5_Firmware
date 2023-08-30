# change below sets to new ones, values are in Hz
rf_path_threshold = 250_000_000
power_amplifier_gain_threshold = 280_000_000



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())


print('Old RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1E38)[0]*10))
print('Old Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAAFC)[0]*10))


fw[0x1E38:0x1E38+4] = struct.pack('<I',rf_path_threshold//10) 
fw[0xAAFC:0xAAFC+4] = struct.pack('<I',power_amplifier_gain_threshold//10)


print('New RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1E38)[0]*10))
print('New Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAAFC)[0]*10))


open(sys.argv[1],'wb').write(fw)
