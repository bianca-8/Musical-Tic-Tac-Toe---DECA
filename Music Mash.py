import simpleaudio as sa

# sound files
a = "a.wav"
b = "b.wav"
c = "c.wav"
d = "d.wav"
e = "e.wav"
f = "f.wav"
g = "g.wav"


wavec = sa.WaveObject.from_wave_file(c)
playc = wavec.play()
playc.wait_done()  # Wait until sound has finished playing

waved = sa.WaveObject.from_wave_file(d)
playd = waved.play()
playd.wait_done()  # Wait until sound has finished playing

wavee = sa.WaveObject.from_wave_file(e)
playe = wavee.play()
playe.wait_done()  # Wait until sound has finished playing

wavef = sa.WaveObject.from_wave_file(f)
playf = wavef.play()
playf.wait_done()  # Wait until sound has finished playing

waveg = sa.WaveObject.from_wave_file(g)
playg = waveg.play()
playg.wait_done()  # Wait until sound has finished playing

wavea = sa.WaveObject.from_wave_file(a)
playa = wavea.play()
playa.wait_done()  # Wait until sound has finished playing

waveb = sa.WaveObject.from_wave_file(b)
playb = waveb.play()
playb.wait_done()  # Wait until sound has finished playing