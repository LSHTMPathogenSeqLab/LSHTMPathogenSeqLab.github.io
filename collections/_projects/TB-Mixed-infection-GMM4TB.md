---
layout: default
name: Mixed infections in genotypic drug-resistant Mycobacterium tuberculosis (GMM4TB)
theme: 
  - TB
  - software
pid: gmm4tb
link: https://www.nature.com/articles/s41598-023-44341-x
people:
  - lwang
  - jphelan
  - tgclark
  - scampino
  
highlighted: false
---
Tuberculosis disease (TB), caused by Mycobacterium tuberculosis, is a major global public health problem, resulting in more than 1 million deaths each year. Drug resistance (DR), including multi-drug (MDR-TB), is making TB control difficult and accounts for 16% of new and 48% of previously treated cases. To further complicate treatment decision-making, many clinical studies have reported patients harbouring multiple distinct strains of M. tuberculosis across the main lineages (L1 to L4). The extent to which drug-resistant strains can be deconvoluted within mixed strain infection samples is understudied. Here, we analysed M. tuberculosis isolates with whole genome sequencing data (n = 50,723), which covered the main lineages (L1 9.1%, L2 27.6%, L3 11.8%, L4 48.3%), with genotypic resistance to isoniazid (HR-TB; n = 9546 (29.2%)), rifampicin (RR-TB; n = 7974 (24.4%)), and at least MDR-TB (n = 5385 (16.5%)). TB-Profiler software revealed 531 (1.0%) isolates with potential mixed sub-lineage infections, including some with DR mutations (RR-TB 21/531; HR-TB 59/531; at least MDR-TB 173/531). To assist with the deconvolution of such mixtures, we adopted and evaluated a statistical Gaussian Mixture model (GMM) approach. By simulating 240 artificial mixtures of different ratios from empirical data across L1 to L4, a GMM approach was able to accurately estimate the DR profile of each lineage, with a low error rate for the estimated mixing proportions (mean squared error 0.012) and high accuracy for the DR predictions (93.5%). Application of the GMM model to the clinical mixtures (n = 531), found that 33.3% (188/531) of samples consisted of DR and sensitive lineages, 20.2% (114/531) consisted of lineages with only DR mutations, and 40.6% (229/531) consisted of lineages with genotypic pan-susceptibility. Overall, our work demonstrates the utility of combined whole genome sequencing data and GMM statistical analysis approaches for providing insights into mono and mixed M. tuberculosis infections, thereby potentially assisting diagnosis, treatment decision-making, drug resistance and transmission mapping for infection control.

The runnable programme can be accessed from author's github: <i>https://github.com/linfeng-wang</i>