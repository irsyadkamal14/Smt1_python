from matplotlib import pyplot
pyplot.plot([1,2,3,4,5,6,7,8,9,10,11,12],
            [32,34,33,31,30,29,27,25,26,28,31,32],)
pyplot.title("Rerata Suhu")
pyplot.xlabel("Bulan")
pyplot.ylabel("Suhu")
pyplot.xticks([1,2,3,4,5,6,7,8,9,10,11,12],
              ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agus","Sep","Okt","Nov","Des"])
pyplot.show()