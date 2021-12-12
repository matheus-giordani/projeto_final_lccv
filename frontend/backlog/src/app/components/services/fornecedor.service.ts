import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Fornecedores } from '../interface/fornecedor.interface';

@Injectable({
  providedIn: 'root'
})
export class FornecedorService {

  constructor(public http: HttpClient) { }

  private httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
  private geralUrl = 'http://localhost:8000/fornecedores/'


  getAll(): Observable<Fornecedores[]> {
    return this.http.get<Fornecedores[]>(this.geralUrl, this.httpOptions)
  }

  get(id: number): Observable<Fornecedores> {
    let url = `${this.geralUrl}/${id}`;
    return this.http.get<Fornecedores>(url)
  }

  create(geral: Fornecedores): Observable<Fornecedores> {
    return this.http.post<Fornecedores>(this.geralUrl, geral, this.httpOptions)
  }

  delete(item: Fornecedores | number): Observable<Fornecedores> {
    const id = typeof item == 'number' ? item : item.id_fornecedor
    const url = `${this.geralUrl}/${id}`;
    return this.http.delete<Fornecedores>(url, this.httpOptions)
  }
  // edit(item: Fornecedores | number) {
  //   const id = typeof item == 'number' ? item : item.id
  // }

  update(item: Fornecedores): Observable<any> {
    const url = `${this.geralUrl}/${item.id_fornecedor}`;
    return this.http.put<Fornecedores>(url, item, this.httpOptions);
  }
}
