import { ItensService } from './itens.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { structItens } from './shared/itens.model';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
  selector: 'app-itens',
  templateUrl: './itens.component.html',
  styleUrls: ['./itens.component.scss']
})
export class ItensComponent implements OnInit {

  itens!: structItens[];
  itensForm!: FormGroup;



  public objeto: string | undefined;


  constructor(private itensService: ItensService, private location: Location) { }


  ngOnInit(): void {









  }
  onSubmit() {





  }







}
