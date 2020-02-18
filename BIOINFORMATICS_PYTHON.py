{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import Bio.Alphabet\n",
    "from Bio.Alphabet import IUPAC\n",
    "from Bio.Seq import Seq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ala', 'Asx', 'Cys', 'Asp', 'Glu', 'Phe', 'Gly', 'His', 'Ile', 'Lys', 'Leu', 'Met', 'Asn', 'Pro', 'Gln', 'Arg', 'Ser', 'Thr', 'Sec', 'Val', 'Trp', 'Xaa', 'Tyr', 'Glx']\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pro_letter=Bio.Alphabet.ThreeLetterProtein.letters;\n",
    "print(pro_letter);\n",
    "print(\"\\n\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ACDEFGHIKLMNPQRSTVWY\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pro_iupac=IUPAC.protein.letters;\n",
    "print(pro_iupac);\n",
    "print(\"\\n\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GATC\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pro_unamb_iupac=IUPAC.unambiguous_dna.letters;\n",
    "print(pro_unamb_iupac);\n",
    "print(\"\\n\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GATCRYWSMKHBVDN\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pro_amb_iupac=IUPAC.ambiguous_dna.letters;\n",
    "print(pro_amb_iupac);\n",
    "print(\"\\n\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ACDEFGHIKLMNPQRSTVWYBXZJUO\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pro_extend_letter=IUPAC.ExtendedIUPACProtein.letters;\n",
    "print(pro_extend_letter);\n",
    "print(\"\\n\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
