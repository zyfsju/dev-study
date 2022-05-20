#### Property Binding
Use brackets in html, and define class attributes in JS.
```html
<!-- app.component.html -->
<input class="form-control" placeholder="Breed" [value]="breed" />
```

```javascript
export class AppComponent {
  title = 'Just Puppers!';
  breed: string = "labrador";
}
```


#### Event Binding
Use parantheses in html and define class methods in JS.
```html
<button class="btn btn-primary" (click)="findDog()">Fetch</button>
```
```javascript
export class AppComponent {
  title = 'Just Puppers!';
  breed: string = "labrador";

  findDog() {
    console.log(this.breed);
  }
}
```

#### Two-way Data Binding
```html
<input class="form-control" placeholder="Breed" [(ngModel)]="breed" />
```

```js
export class AppComponent {
  title = 'Just Puppers!';
  breed: string = "labrador";

  findDog() {
    console.log(this.breed);
  }
}
```

#### Services and HTTP requests
```javascript
// dog.service.ts
import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

interface BreedSingleImageResponse {
  message: string;
  status: string;
}
@Injectable({
  providedIn: 'root'
})
export class DogService {

  constructor(private http: HttpClient) { }

  findDog(breed: string, subBreed?: string): Observable<BreedSingleImageResponse> {
    const endpoint = subBreed ?
    `https://dog.ceo/api/breed/${breed}/${subBreed}/images/random`:
    `https://dog.ceo/api/breed/${breed}/images/random`;
  
    return this.http.get<BreedSingleImageResponse>(endpoint);
  }
}
```


```js

```

#### Conditional Rendering with ngIf

#### Navigation with routing
```bash
ng g c dog-form # generate a component
ng generate service dog
```

**Question**: `constructor` vs `ngOnInit`


