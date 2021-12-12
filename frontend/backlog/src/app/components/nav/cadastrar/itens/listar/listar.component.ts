import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ItensService } from './../itens.service';
import { Component, OnInit } from '@angular/core';
import { structItens } from '../shared/itens.model';
import { Location } from '@angular/common';
import { Router } from '@angular/router'
@Component({
  selector: 'app-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.scss']
})
export class ListarComponent implements OnInit {
  componentsItens!: structItens[];
  editFormItens!: FormGroup;
  somaTotal!: number
  componentsItens2!: structItens[]
  router: any;



  constructor(private itensService: ItensService, private location: Location) { }

  ngOnInit(): void {
    this.itensService.getAll().subscribe(f => this.componentsItens = f)






  }
  del(item: structItens, idx: number) {
    if (confirm("Deseja excluir este item?")) {
      this.itensService.delete(item).subscribe(_ => this.componentsItens.splice(idx, 1))

    }


  }
  edit(id: number) {
    this.itensService.get(id).subscribe(f => this.creatForm(f))


  }

  creatForm(f: structItens) {
    this.editFormItens = new FormGroup({
      'servico': new FormControl('', [Validators.required]),//Validators.required coloca campo como obrigatorio
      'quantidade': new FormControl('', [Validators.required]),
      'valor_unitario': new FormControl('', [Validators.required]),
      'valor_total': new FormControl(),
      'id': new FormControl()

    })
    // this.editFormItens.controls['valor_total'].disable()
  }

  onSubmit() {
    const vlrTotal = this.editFormItens.controls['valor_unitario'].value * this.editFormItens.controls['quantidade'].value;
    this.editFormItens.patchValue({ valor_total: vlrTotal });
    const newRegister = this.editFormItens.value;
    this.itensService.update(newRegister)
      .subscribe();
    window.location.reload()



  }



}
