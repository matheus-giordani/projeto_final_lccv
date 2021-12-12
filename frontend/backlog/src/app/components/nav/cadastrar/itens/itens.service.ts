import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { structItens } from './shared/itens.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ItensService {
  reload = true;

  constructor(public http: HttpClient) { }

  private httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
  private itensUrl = "http://localhost:3000/itens"


  getAll(): Observable<structItens[]> {
    return this.http.get<structItens[]>(this.itensUrl, this.httpOptions)
  }

  get(id: number): Observable<structItens> {
    let url = `${this.itensUrl}/${id}`;
    return this.http.get<structItens>(url)
  }


  create(itens: structItens): Observable<structItens> {
    return this.http.post<structItens>(this.itensUrl, itens, this.httpOptions)
  }

  delete(item: structItens | number): Observable<structItens> {
    const id = typeof item == 'number' ? item : item.tombamento
    const url = `${this.itensUrl}/${id}`;
    return this.http.delete<structItens>(url, this.httpOptions)
  }

  update(itens: structItens): Observable<any> {
    const url = `${this.itensUrl}/${itens.id_estado_bem}`;
    return this.http.put<structItens>(url, itens, this.httpOptions);
  }


}
