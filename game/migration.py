import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy1 = ducks.Duck()
daisy2 = ducks.Duck()
daisy3 = ducks.Duck()
daisy4 = ducks.Duck()
daisy5 = ducks.Duck()
daisy6 = ducks.Duck()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy1)
flock.add_duck(daisy2)
flock.add_duck(daisy3)
flock.add_duck(percy)
flock.add_duck(daisy4)
flock.add_duck(daisy5)
flock.add_duck(daisy6)

flock.migrate()
