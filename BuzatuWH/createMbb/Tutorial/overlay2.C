{
  std::vector<std::string> vec_string={"Nominal","Parton","OneMu","PtRecoBukin", "Regression"};
  TFile* output = new TFile("histos.root","RECREATE");
  std::map<std::string,TH1F*> map_string_TH1F;
  for(int i=0; i!=vec_string.size(); i++){
    std::string name=vec_string.at(i);
    std::cout<<"name="<<name<<std::endl;
    map_string_TH1F[name]= new TH1F(name.c_str(), name.c_str(), 30, 0.0,1.5);
    map_string_TH1F[name]->SetLineColor(i+1);
    perjet->Project(name.c_str(),(name+"_Pt/Parton_Pt").c_str());
  }//end loop over variations
  output->Write();
  output->Close();
}
