from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/search',methods=['POST'])
def binary_search():
 data=request.get_json()
 arr=data['array']
 target=data['target']
 left=0
 right=len(arr)-1
 while left<=right:
  mid=(left+right)//2
  if arr[mid]==target: return jsonify({'index':mid})
  if arr[mid]<target: left=mid+1
  else: right=mid-1
 return jsonify({'index':-1})
