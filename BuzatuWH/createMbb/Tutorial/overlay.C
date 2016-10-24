{
  std::vector<std::string> vec_string={"Nominal_Pt","Parton_Pt","OneMu_Pt","PtRecoBukin_Pt"};
  //TFile* output = new TFile("histos.root","RECREATE");
  std::map<std::string,TH1F*> map_string_TH1F;
  for(int i=0; i!=vec_string.size(); i++){
    std::string name=vec_string.at(i);
    std::cout<<"name="<<name<<std::endl;
    map_string_TH1F[name]= new TH1F(name.c_str(), name.c_str(), 20, 0, 200);
    map_string_TH1F[name]->SetLineColor(i+1);
    perjet->Project(name.c_str(),name.c_str());
  }//end loop over variations
  //output->Write();
  //output->Close();
  //plot histograms
  TCanvas* c = new TCanvas ("c","c",600,600);
  for(int i=0; i!=vec_string.size(); i++){
    std::string name=vec_string.at(i);
    std::cout<<"name="<<name<<std::endl;
    std::string draw_option="";
    if (i!=0) {
      draw_option+="same";
    }
    map_string_TH1F[name.c_str()]->Draw(draw_option.c_str());
  }
  c->Print("c.pdf");






}
