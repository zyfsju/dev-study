### CI/CD

#### Gitlab

`.gitlab-ci.yml`

```yaml
image: python:3.7-alpine

stages:
    - test

# before_script:
#   - source $WORK_DIR/vst-env/bin/activate
#   - pip install my_common/

test:
    stage: test
    script:
        - echo "HELLO!"
        - docker build -t my-common --build-arg CACHEBUST=$(date +%s) my_common
    tags:
        - my-gitlab-runner # gitlab runner
```
