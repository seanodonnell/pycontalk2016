Some short scripts for demonstrating cprofile

To profile the two scripts run:

python -m cProfile -o profile_output_1 prime1.py
python -m cProfile -o profile_output_2 prime2.py

To view a visualization of the results

pip install -r requirements.txt

runsnake profile_output_1
runsnake profile_output_2
