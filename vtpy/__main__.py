import sys, pprint, vt

results = vt.analyze(sys.argv[1])
if results is None:
  print("Upload or analysis failed.")
else:
  pprint.PrettyPrinter(indent=4).print(results)