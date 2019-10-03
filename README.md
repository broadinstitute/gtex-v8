## GTEx V8 

This repository contains notebooks and scripts for reproducing analyses and figures from the paper [The GTEx Consortium atlas of genetic regulatory effects across human tissues](https://www.biorxiv.org/content/).


#### Requirements
The following Python modules are needed to run the notebooks:
`numpy, pandas, scipy, ipython, jupyter, matplotlib, seaborn, qtl`

The notebooks require data from the [GTEx Portal](https://gtexportal.org) to run (by default, the data is assumed to be accessible in the `data` directory of this repository). Running the following commands will download the relevant files:
```
cd data

# QTLs
wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_eQTL.tar && \
    tar xf GTEx_Analysis_v8_eQTL.tar && rm GTEx_Analysis_v8_eQTL.tar

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_sQTL.tar && \
    tar xf GTEx_Analysis_v8_sQTL.tar && rm GTEx_Analysis_v8_sQTL.tar

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_eQTL_independent.tar && \
    tar xf GTEx_Analysis_v8_eQTL_independent.tar && rm GTEx_Analysis_v8_eQTL_independent.tar

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_sQTL_independent.tar && \
    tar xf GTEx_Analysis_v8_sQTL_independent.tar && rm GTEx_Analysis_v8_sQTL_independent.tar

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_trans_eGenes_fdr05.txt

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_trans_sGenes_fdr05.txt

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_eQTL_expression_matrices.tar && \
    tar xf GTEx_Analysis_v8_eQTL_expression_matrices.tar && rm GTEx_Analysis_v8_eQTL_expression_matrices.tar

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_eQTL_covariates.tar.gz && \
    tar xf GTEx_Analysis_v8_eQTL_covariates.tar.gz && rm GTEx_Analysis_v8_eQTL_covariates.tar.gz

wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_Analysis_v8_sQTL_groups.tar.gz && \
    tar xf GTEx_Analysis_v8_sQTL_groups.tar.gz && rm GTEx_Analysis_v8_sQTL_groups.tar.gz

# fine mapping results
wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_v8_finemapping_CAVIAR.tar && \
    tar xf GTEx_v8_finemapping_CAVIAR.tar && rm GTEx_v8_finemapping_CAVIAR.tar
wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_v8_finemapping_CaVEMaN.tar && \
    tar xf GTEx_v8_finemapping_CaVEMaN.tar && rm GTEx_v8_finemapping_CaVEMaN.tar
wget https://storage.googleapis.com/gtex_analysis_v8/single_tissue_qtl_data/GTEx_v8_finemapping_DAPG.tar && \
    tar xf GTEx_v8_finemapping_DAPG.tar && rm GTEx_v8_finemapping_DAPG.tar

# annotation
wget https://storage.googleapis.com/gtex_analysis_v8/reference/gencode.v26.GRCh38.genes.gtf
wget https://storage.googleapis.com/gtex_analysis_v8/reference/WGS_Feature_overlap_collapsed_VEP_short_4torus.MAF01.txt.gz
```

A subset of the figures require genotype information. The VCF can be obtained from dbGaP (accession [phs000424](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000424)) of from [AnVIL](https://anvil.terra.bio/#workspaces/anvil-datastorage/AnVIL_GTEx_V8_hg38) (requires dbGaP authentication).
