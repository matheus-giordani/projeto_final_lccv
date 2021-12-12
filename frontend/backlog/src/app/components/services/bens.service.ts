
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Bens } from '../interface/bens.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BensService {

  constructor(public http: HttpClient) { }

  private httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
  private geralUrl = 'http://localhost:8000/bens/'


  getAll(): Observable<Bens[]> {
    return this.http.get<Bens[]>(this.geralUrl, this.httpOptions)
  }

  get(id: number): Observable<Bens> {
    let url = `${this.geralUrl}/${id}`;
    return this.http.get<Bens>(url)
  }

  create(geral: Bens): Observable<Bens> {
    return this.http.post<Bens>(this.geralUrl, geral, this.httpOptions)
  }

  delete(item: Bens | number): Observable<Bens> {
    const id = typeof item == 'number' ? item : item.id_bem
    const url = `${this.geralUrl}/${id}`;
    return this.http.delete<Bens>(url, this.httpOptions)
  }
  // edit(item: Bens | number) {
  //   const id = typeof item == 'number' ? item : item.id
  // }

  update(item: Bens): Observable<any> {
    const url = `${this.geralUrl}/${item.id_bem}`;
    return this.http.put<Bens>(url, item, this.httpOptions);
  }


}
