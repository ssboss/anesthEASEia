clear;
clc;

% loading the data form xml to csv
casex = readstruct("case1.xml");

% breaks down the csv file
casex_table = struct2table(casex);
casex_table_operation = struct2table(casex.operation);
casex_table_patient = struct2table(casex.patient);
casex_table_events = struct2table(casex.events);
casex_table_drugs = struct2table(casex.drugs);
casex_table_data = struct2table(casex.data);

% a easier table to extract data from
casex_new_table = [casex_table casex_table_patient casex_table_events casex_table_drugs casex_table_data];

