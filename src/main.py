import csv
import requests
import json

from settings import Settings

settings = Settings()


def import_csv_as_tuples(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = [tuple(row) for row in csv_reader]
    return data


def get_dataset_files(sample):
    token = settings.token
    headers = {"Authorization": "Bearer " + token}

    url_fastq = settings.base_url + "datasets/" + settings.dataset_id + "/files?pipelineId=" + settings.raw_pipeline_id + "&subfolder=fastq&sampleId=" + sample[0]
    url_bam = settings.base_url + "datasets/" + settings.dataset_id + "/files?pipelineId=" + settings.processed_pipeline_id + "&subfolder=bam&sampleId=" + sample[0]
    url_vcf = settings.base_url + "datasets/" + settings.dataset_id + "/files?pipelineId=" + settings.processed_pipeline_id + "&subfolder=vcf&sampleId=" + sample[0]

    print(url_fastq)
    print(url_bam)
    print(url_vcf)

    fastq_files = requests.get(url_fastq, headers=headers, verify=False).json()
    bam_files = requests.get(url_bam, headers=headers, verify=False).json()
    vcf_files = requests.get(url_vcf, headers=headers, verify=False).json()

    print(fastq_files)
    print(bam_files)
    print(vcf_files)

    fastq_file_names = []
    bam_file_names = []
    vcf_file_names = []

    for file_fastq in fastq_files["fastq"]:
        fastq_file_names.append(file_fastq["name"])

    for file_bam in bam_files["bam"]:
        bam_file_names.append(file_bam["name"])

    for file_vcf in vcf_files["vcf"]:
        vcf_file_names.append(file_vcf["name"])

    return fastq_file_names, bam_file_names, vcf_file_names


def main():
    samples = import_csv_as_tuples("../samples.csv")
    print(samples)

    for sample in samples:
        fastq_files_names, bam_file_names, vcf_file_names = get_dataset_files(sample)
        print(fastq_files_names)
        print(bam_file_names)
        print(vcf_file_names)


if __name__ == "__main__":
    main()
