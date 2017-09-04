# -*- coding:utf-8 -*-
import logging
from falcon.status_codes import HTTP_BAD_REQUEST, HTTP_NOT_FOUND, HTTP_FORBIDDEN

logger = logging.getLogger(__name__)


class ApiError(Exception):
    code = 0
    code_name = 'Api Runtime Error'
    message = 'Runtime api error occurred.'
    status = HTTP_BAD_REQUEST

    def __init__(self, message=None, code=None, code_name=None, *args, **kwargs):
        super(ApiError, self).__init__(*args, **kwargs)
        if message:
            self.message = message
        if code is not None:
            self.code = code
        if code_name is not None:
            self.code_name = code_name

    def to_dict(self, *args, **kwargs):
        result = {
            'err_code': self.code,
            'err_name': self.code_name,
            'message': self.message
        }
        logging.info("Return Error:{0}".format(result))
        return result


# 参数类错误401xxx
class ErrorInvalidArgument(ApiError):
    """
    参数缺失或错误
    """
    code = 401001
    code_name = 'Invalid_Argument'
    zh_message = '参数缺失或错误.'


class ErrorNameAlreadyExist(ApiError):
    """
    name已存在
    """
    code = 401002
    code_name = 'Name_Already_Exist'
    message = 'name already exist.'
    zh_message = '名称已存在.'


class ErrorAccountAlreadyExist(ApiError):
    """
    account已存在
    """
    code = 401003
    code_name = 'Account_Already_Exist'
    message = 'account already exist.'
    zh_message = '账号已存在.'


class ErrorMobileAlreadyExist(ApiError):
    """
    mobile已存在
    """
    code = 401004
    code_name = 'Mobile_Already_Exist'
    message = 'mobile already exist.'
    zh_message = '手机号码已存在.'


class ErrorCodeAlreadyExist(ApiError):
    """
    code已存在
    """
    code = 401005
    code_name = 'Code_Already_Exist'
    message = 'code already exist.'
    zh_message = 'code已存在.'


class ErrorMobileNotFound(ApiError):
    """
    手机号没有找到
    """
    code = 401006
    code_name = 'Mobile_Not_Found'
    message = 'mobile not found.'
    zh_message = '手机号码没有找到.'


class ErrorSellerOrderIdAlreadyExist(ApiError):
    """
    商户订单编号已存在
    """
    code = 401007
    code_name = 'Seller_Order_Id_Already_Exist'
    message = 'seller order id already exist.'
    zh_message = '订单已存在.'


class ErrorVerifyCodeErr(ApiError):
    """
    验证码错误
    """
    code = 401008
    code_name = 'Verify_Code_Err'
    message = 'verify code err.'
    zh_message = '验证码错误.'


class ErrorShortNameAlreadyExist(ApiError):
    """
    简称已存在
    """
    code = 401009
    code_name = 'Short_Name_Already_Exist'
    message = 'short name already exist.'
    zh_message = '简称已存在.'


class ErrorGetPoiFailed(ApiError):
    """
    获取地址经纬度失败
    """
    code = 401010
    code_name = 'Get_Poi_Failed'
    message = 'get poi failed'
    zh_message = '获取地址经纬度失败.'


class ErrorPoiOutRange(ApiError):
    """
    地址超区
    """
    code = 401011
    code_name = 'Poi_Out_Of_Range'
    message = 'poi out of range'
    zh_message = '地址超出配送范围.'


# 服务商类错误402xxx
class ErrorVendorCreateFailed(ApiError):
    """
    服务商创建失败
    """
    code = 402001
    code_name = 'Vendor_Create_Failed'
    message = 'vendor create failed.'
    zh_message = '服务商创建失败.'


class ErrorVendorUpdateFailed(ApiError):
    """
    服务商更新错误
    """
    code = 402002
    code_name = 'Vendor_Update_Failed'
    message = 'vendor update failed.'
    zh_message = '服务商更新失败.'


class ErrorVendorNotFound(ApiError):
    """
    服务商没有找到
    """
    code = 402003
    code_name = 'Vendor_Not_Found'
    message = 'vendor not found.'
    zh_message = '服务商没有找到.'


class ErrorVendorStateUnavailable(ApiError):
    """
    服务商状态不可用
    """
    code = 402004
    code_name = 'Vendor_State_Unavailable'
    message = 'vendor state unavailable.'
    zh_message = '服务商不可用（状态错误）.'


class ErrorVendorVerifyStateUnavailable(ApiError):
    """
    服务商未审核通过
    """
    code = 402005
    code_name = 'Vendor_Verify_State_Unavailable'
    message = 'vendor verify state unavailable.'
    zh_message = '服务商未审核通过.'


class ErrorVendorNotBusinessHours(ApiError):
    """
    不在配送时间内
    """
    code = 402006
    code_name = 'Vendor_Not_Business_Hours'
    message = 'vendor not business hours.'
    zh_message = '不在配送时间内.'


class ErrorVendorStateError(ApiError):
    """
    服务商状态错误
    """
    code = 402007
    code_name = 'Vendor_State_Error'
    message = 'vendor state error.'
    zh_message = '服务商状态错误.'


# 商户类错误403xxx
class ErrorSellerCreateFailed(ApiError):
    """
    商户创建失败
    """
    code = 403001
    code_name = 'Seller_Create_Failed'
    message = 'seller create failed.'
    zh_message = '商户创建失败.'


class ErrorSellerUpdateFailed(ApiError):
    """
    商户更新失败
    """
    code = 403002
    code_name = 'Seller_Update_Failed'
    message = 'seller update failed.'
    zh_message = '商户信息更新失败.'


class ErrorSellerNotFound(ApiError):
    """
    商户没有找到
    """
    code = 403003
    code_name = 'Seller_Not_Found'
    message = 'seller not found.'
    zh_message = '商户没有找到.'


class ErrorSellerStateUnavailable(ApiError):
    """
    商户被禁用
    """
    code = 403004
    code_name = 'Seller_State_Unavailable'
    message = 'seller state unavailable.'
    zh_message = '商户被禁用.'


class ErrorSellerVerifyStateUnavailable(ApiError):
    """
    商户未审核通过,或商户审核状态错误
    """
    code = 403005
    code_name = 'Seller_Verify_State_Unavailable'
    message = 'seller verify state unavailable.'
    zh_message = '商户未审核通过.'


class ErrorSellerNotSign(ApiError):
    """
    商户未签约
    """
    code = 403006
    code_name = 'Seller_Not_Sign'
    message = 'seller not sign.'
    zh_message = '商户未签约.'


class ErrorSellerSignFailed(ApiError):
    """
    商户签约失败
    """
    code = 403007
    code_name = 'Seller_Sign_Failed'
    message = 'seller sign failed.'
    zh_message = '商户签约失败.'

class ErrorSellerUpdateForbidden(ApiError):
    """
    商户禁止编辑
    """
    code = 403008
    code_name = 'Seller_Update_Forbidden'
    message = 'seller update forbidden.'
    zh_message = '商户不允许编辑.'


class ErrorSellerAlreadySign(ApiError):
    """
    商户已签约该产品
    """
    code = 403009
    code_name = 'Seller_Already_Sign'
    message = 'seller already sign.'
    zh_message = '商户已签约该产品.'


class ErrorSellerUnsignedFailed(ApiError):
    """
    商户解约失败
    """
    code = 403010
    code_name = 'Seller_Unsigned_Failed'
    message = 'seller unsigned failed.'
    zh_message = '商户解约失败.'


class ErrorContractNotFound(ApiError):
    """
    未找到签约记录
    """
    code = 403011
    code_name = 'Contract_Not_Found'
    message = 'contract not found.'
    zh_message = '未找到签约记录.'


class ErrorContractStateError(ApiError):
    """
    签约记录状态错误
    """
    code = 403012
    code_name = 'Contract_State_Error'
    message = 'contract state error.'
    zh_message = '签约记录状态错误.'

# 区域,区域类错误404xxx
class ErrorAreaCreateFailed(ApiError):
    """
    区域创建失败
    """
    code = 404001
    code_name = 'Area_Create_Failed'
    message = 'area create failed.'
    zh_message = '区域创建失败.'


class ErrorAreaUpdateFailed(ApiError):
    """
    区域更新失败
    """
    code = 404002
    code_name = 'Area_Update_Failed'
    message = 'area update failed.'
    zh_message = '区域更新失败.'


class ErrorAreaNotFound(ApiError):
    """
    区域没有找到
    """
    code = 404003
    code_name = 'Area_Not_Found'
    message = 'area not found.'
    zh_message = '区域没有找到.'


class ErrorAreaState(ApiError):
    """
    区域状态错误
    """
    code = 404004
    code_name = 'Area_State_Error'
    message = 'area state error.'
    zh_message = '区域状态错误.'


class ErrorAreaPublishFailed(ApiError):
    """
    区域发布失败
    """
    code = 404005
    code_name = 'Area_Publish_Failed'
    message = 'area publish failed.'
    zh_message = '区域发布失败.'


class ErrorParentAreaNotFound(ApiError):
    """
    父区域没有找到
    """
    code = 404006
    code_name = 'Parent_Area_Not_Found'
    message = 'parent area not found.'
    zh_message = '父区域没有找到.'


class ErrorRegionCreateFailed(ApiError):
    """
    区域围栏创建失败
    """
    code = 404007
    code_name = 'Region_Create_Failed'
    message = 'region create failed.'
    zh_message = '区域围栏创建失败.'


class ErrorRegionUpdateFailed(ApiError):
    """
    区域围栏更新失败
    """
    code = 404008
    code_name = 'Region_Update_Failed'
    message = 'region update failed.'
    zh_message = '区域围栏更新失败.'


class ErrorRegionNotFound(ApiError):
    """
    区域围栏没有找到
    """
    code = 404009
    code_name = 'Region_Not_Found'
    message = 'region not found'
    zh_message = '区域围栏没有找到.'


# 产品类错误405xxx
class ErrorServiceCreateFailed(ApiError):
    """
    产品创建失败
    """
    code = 405001
    code_name = 'Service_Create_Failed'
    message = 'service create failed.'
    zh_message = '产品创建失败.'


class ErrorServiceUpdateFailed(ApiError):
    """
    产品更新失败
    """
    code = 405002
    code_name = 'Service_Update_Failed'
    message = 'service update failed.'
    zh_message = '产品更新失败.'


class ErrorServiceNotFound(ApiError):
    """
    产品没有找到
    """
    code = 405003
    code_name = 'Service_Not_Found'
    message = 'service not found.'
    zh_message = '产品没有找到.'


class ErrorServiceUnavailable(ApiError):
    """
    产品不可用
    """
    code = 405004
    code_name = 'Service_Unavailable'
    message = 'service unavailable.'
    zh_message = '产品不可用.'


class ErrorServiceActiveFailed(ApiError):
    """
    产品启用失败
    """
    code = 405005
    code_name = 'Service_Active_Failed'
    message = 'service active failed.'
    zh_message = '产品启用失败.'


class ErrorServiceStateError(ApiError):
    """
    产品状态错误
    """
    code = 405006
    code_name = 'Service_State_Error'
    message = 'service state error'
    zh_message = '产品状态错误.'


class ErrorServiceAlreadyExistEnable(ApiError):
    """
    产品已启用
    """
    code = 405007
    code_name = 'Service_Already_Exist_Enable'
    message = 'service already exist enable.'
    zh_message = '产品已起用.'


class ErrorServiceVersionNotFound(ApiError):
    """
    产品版本没有找到
    """
    code = 405008
    code_name = 'Service_Version_Not_Found'
    message = 'service version not found.'
    zh_message = '产品版本没有找到.'


class ErrorServiceVersionStateError(ApiError):
    """
    产品状态错误
    """
    code = 405006
    code_name = 'Service_Version_State_Error'
    message = 'service version state error'
    zh_message = '产品状态错误.'


# 账号类错误407xxx
class ErrorAccountCreateFailed(ApiError):
    """
    账号创建失败
    """
    code = 407001
    code_name = 'Account_Create_Failed'
    message = 'account create failed.'
    zh_message = '账号创建失败.'


class ErrorAccountUpdateFailed(ApiError):
    """
    账号更新失败
    """
    code = 407002
    code_name = 'Account_Update_Failed'
    message = 'account update failed.'
    zh_message = '账号更新失败.'


class ErrorAccountNotFound(ApiError):
    """
    账号没有找到
    """
    code = 407003
    code_name = 'Account_Not_Found'
    message = 'account not found.'
    zh_message = '账号没有找到.'


class ErrorAccountIsDisable(ApiError):
    """
    账号不可用
    """
    code = 407004
    code_name = 'Account_Is_Disable'
    message = 'account is disable.'
    zh_message = '账号不可用.'


class ErrorAccountAclNotFound(ApiError):
    """
    账号权限没有找到
    """
    code = 407005
    code_name = 'Account_Acl_Not_Found'
    message = 'account acl not found.'
    zh_message = '账号权限没有找到.'


# 登录,注册类错误408xxx
class ErrorLoginFailed(ApiError):
    """
    登录失败
    """
    code = 408001
    code_name = 'Login_Failed'
    message = 'login failed.'
    zh_message = '登录失败.'


class ErrorRegisterFailed(ApiError):
    """
    注册失败
    """
    code = 408002
    code_name = 'Register_Failed'
    message = 'register failed.'
    zh_message = '注册失败.'


# 骑士类错误409xxx
class ErrorCourierCreateFailed(ApiError):
    """
    骑士创建失败
    """
    code = 409001
    code_name = 'Courier_Create_Failed'
    message = 'courier create failed.'
    zh_message = '骑士创建失败.'


class ErrorCourierUpdateFailed(ApiError):
    """
    骑士更新失败
    """
    code = 409002
    code_name = 'Courier_Update_Failed'
    message = 'courier update failed.'
    zh_message = '骑士更新失败.'


class ErrorCourierNotFound(ApiError):
    """
    骑士没有找到
    """
    code = 409003
    code_name = 'Courier_Not_Found'
    message = 'courier not found.'
    zh_message = '骑士没有找到.'


class ErrorCourierStateError(ApiError):
    """
    骑士状态错误
    """
    code = 409004
    code_name = 'Courier_State_Error'
    message = 'courier state error.'
    zh_message = '骑士状态错误.'


class ErrorCourierVerifyStateError(ApiError):
    """
    骑士审核状态错误
    """
    code = 409005
    code_name = 'Courier_Verify_State_Error'
    message = 'courier verify state error.'
    zh_message = '骑士审核状态错误.'


class ErrorCourierCaptureFailed(ApiError):
    """
    骑士抢单失败
    """
    code = 400320
    code_name = 'Courier_Capture_Shipment_Failed'
    message = 'courier capture shipment failed'
    zh_message = '骑士抢单失败.'


class ErrorCourierOnlineFailed(ApiError):
    """
    骑士上岗失败
    """
    code = 409006
    code_name = 'Courier_Online_Failed'
    message = 'courier online failed'
    zh_message = '骑士上岗失败.'


class ErrorCourierOfflineFailed(ApiError):
    """
    骑士离岗失败
    """
    code = 409007
    code_name = 'Courier_Offline_Failed'
    message = 'courier offline failed'
    zh_message = '骑士离岗失败.'


# 订单类错误410xxx
class ErrorOrderCreateFailed(ApiError):
    """
    订单发单失败
    """
    code = 410001
    code_name = 'Order_Create_Failed'
    message = 'order create failed.'
    zh_message = '订单发单失败.'


class ErrorOrderNotFound(ApiError):
    """
    订单没有找到
    """
    code = 410002
    code_name = 'Order_Not_Found'
    message = 'order not found.'
    zh_message = '订单没有找到.'


class ErrorOrderStateError(ApiError):
    """
    订单状态错误
    """
    code = 410003
    code_name = 'Order_State_Error'
    message = 'order state error.'
    zh_message = '订单状态错误.'


class ErrorOrderCloseDisable(ApiError):
    """
    订单不允许关闭
    """
    code = 410004
    code_name = 'Order_Close_Disable'
    message = 'order close disable.'
    zh_message = '订单不允许关闭.'


class ErrorOrderCloseFailed(ApiError):
    """
    订单关闭失败
    """
    code = 410005
    code_name = 'Order_Close_Failed'
    message = 'order close failed.'
    zh_message = '订单关闭失败.'


class ErrorOrderIrresistibleSingle(ApiError):
    """
    订单不可催单
    """
    code = 410006
    code_name = 'Order_Irresistible_Single'
    message = 'order irresistible single.'
    zh_message = '订单不可催单.'


class ErrorOrderReminderFailed(ApiError):
    """
    订单催单失败
    """
    code = 410007
    code_name = 'Order_Reminder_Failed'
    message = 'Order reminder failed.'
    zh_message = '订单催单失败.'


class ErrorOrderUrgeTimeError(ApiError):
    """
    订单催单时间错误
    """
    code = 410018
    code_name = 'Order_urge_time_error'
    message = 'Order urge time error.'
    zh_message = '订单催单时间错误.'


class ErrorOrderEstimateFeeFailed(ApiError):
    """
    订单配送费估算失败
    """
    code = 410008
    code_name = 'Order_Estimate_Fee_Failed'
    message = 'order estimate fee failed.'
    zh_message = '订单配送费估算失败.'


class ErrorOrderConsigneeOutRange(ApiError):
    """
    订单收货地超出配送区域
    """
    code = 410009
    code_name = 'Order_Consignee_Out_Range'
    message = 'order consignee out range.'
    zh_message = '订单收货地址超出配送区域.'


class ErrorOrderConsigneeRulingRangeFailed(ApiError):
    """
    订单收货地判区失败
    """
    code = 410010
    code_name = 'Order_Consignee_Ruling_Range_Failed'
    message = 'order consignee ruling range failed.'
    zh_message = '订单收货地址判区失败.'


class ErrorOrderConsignorOutRange(ApiError):
    """
    订单发货地超出配送区域
    """
    code = 410011
    code_name = 'Order_Consignor_Out_Range'
    message = 'order consignor out range.'
    zh_message = '订单发货地址超出配送区域.'


class ErrorOrderConsignorRulingRangeFailed(ApiError):
    """
    订单发货地判区失败
    """
    code = 410012
    code_name = 'Order_Consignor_Ruling_Range_Failed'
    message = 'order consignor ruling range failed.'
    zh_message = '订单发货地址判区失败.'


class ErrorOrderDistanceFailed(ApiError):
    """
    订单配送距离计算失败
    """
    code = 410013
    code_name = 'Order_Distance_Failed'
    message = 'order distance failed.'
    zh_message = '订单配送距离计算失败.'


class ErrorOrderOutRange(ApiError):
    """
    订单超出配送区域
    """
    code = 410014
    code_name = 'Order_Out_Range'
    message = 'order out range.'
    zh_message = '订单超出配送区域.'


class ErrorUploadTaskNotFound(ApiError):
    """
    上传任务不存在
    """
    code = 410015
    code_name = 'Upload_Task_Not_Found'
    message = 'upload task not found.'
    zh_message = '上传任务不存在.'


class ErrorUploadTaskStateError(ApiError):
    """
    上传任务状态错误
    """
    code = 410016
    code_name = 'Upload_Task_State_Error'
    message = 'upload task state error.'
    zh_message = '上传任务状态错误.'


class ErrMaxDistanceRange(ApiError):
    """
    订单超出最大配送距离
    """
    code = 410017
    code_name = 'Max_Distance_Range'
    message = 'max distance range.'
    zh_message = '订单超出最大配送距离.'


# 运单类错误411xxx
class ErrorShipmentNotFound(ApiError):
    """
    运单没有找到
    """
    code = 411001
    code_name = 'Shipment_Not_Found'
    message = 'shipment not found.'
    zh_message = '运单没有找到.'


class ErrorShipmentMarkErrorFailed(ApiError):
    """
    运单标记异常失败
    """
    code = 411002
    code_name = 'Shipment_Mark_Error_Failed'
    message = 'shipment mark error failed'
    zh_message = '运单标记异常失败.'


class ErrorShipmentTimeOut(ApiError):
    """
    运单已超时
    """
    code = 411003
    code_name = 'Shipment_Time_Out'
    message = 'shipment time out'
    zh_message = '运单已超时.'


class ErrorShipmentAlreadyCaptured(ApiError):
    """
    运单已抢
    """
    code = 411004
    code_name = 'Shipment_Already_Captured'
    message = 'shipment already captured'
    zh_message = '运单已抢.'


class ErrorShipmentStateError(ApiError):
    """
    运单状态错误
    """
    code = 411005
    code_name = 'Shipment_State_Error'
    message = 'shipment state error'
    zh_message = '运单状态错误.'


class ErrorShipmentReassignSelf(ApiError):
    """
    运单不能改派给自己
    """
    code = 411006
    code_name = 'Shipment_Reassign_Self'
    message = 'shipment reassign self'
    zh_message = '运单不能改派给自己.'


class ErrorShipmentMarkRestoreFailed(ApiError):
    """
    运单取消标记异常
    """
    code = 411007
    code_name = 'Shipment_Mark_Restore_Failed'
    message = 'shipment mark restore failed'
    zh_message = '运单取消标记异常失败.'


class ErrorShipmentClosedType(ApiError):
    """
    运单关闭类型错误
    """
    code = 411008
    code_name = 'Shipment_Closed_Type_Error'
    message = 'shipment closed type error'
    zh_message = '运单关闭类型错误.'


class ErrorShipmentUndone(ApiError):
    """
    运单未完成
    """
    code = 411009
    code_name = 'Shipment_Undone'
    message = 'shipment undone.'
    zh_message = '运单未完成.'


class ErrorShipmentForbiddenCapture(ApiError):
    """
    落地配模式订单不支持抢单
    """
    code = 411010
    code_name = 'Shipment_Forbidden_Capture'
    message = 'shipment forbidden capture.'
    zh_message = '落地配模式订单不支持抢单.'


# 角色类错误412xxx
class ErrorRoleCreateFailed(ApiError):
    """
    角色创建
    """
    code = 412001
    code_name = 'Role_Create_Failed'
    message = 'role create failed.'
    zh_message = '角色创建失败.'


class ErrorRoleUpdateFailed(ApiError):
    """
    角色更新失败
    """
    code = 412002
    code_name = 'Role_Update_Failed'
    message = 'role update failed.'
    zh_message = '角色更新失败.'


class ErrorRoleNotFound(ApiError):
    """
    角色没有找到
    """
    code = 412003
    code_name = 'Role_not_found'
    message = 'role not found.'
    zh_message = '角色没有找到.'


# 权限类错误413xxx
class ErrorPermissionCreateFailed(ApiError):
    """
    权限创建失败
    """
    code = 413001
    code_name = 'Permission_Create_Failed'
    message = 'Permission create failed.'
    zh_message = '权限创建失败.'


class ErrorPermissionUpdateFailed(ApiError):
    """
    权限更新失败
    """
    code = 413002
    code_name = 'Permission_Update_Failed'
    message = 'Permission update failed.'
    zh_message = '权限更新失败.'


class ErrorPermissionNotFound(ApiError):
    """
    权限没有找到
    """
    code = 413003
    code_name = 'Permission_not_found'
    message = 'permission not found.'
    zh_message = '权限没有找到.'


# 店铺类错误414xxx
class ErrorShopCreateFailed(ApiError):
    """
    店铺创建失败
    """
    code = 414001
    code_name = 'Shop_Create_Failed'
    message = 'shop create failed.'
    zh_message = '店铺创建失败.'


class ErrorShopUpdateFailed(ApiError):
    """
    店铺更新失败
    """
    code = 414002
    code_name = 'Shop_Update_Failed'
    message = 'shop update failed.'
    zh_message = '店铺更新失败.'


class ErrorShopNotFound(ApiError):
    """
    店铺没有找到
    """
    code = 414003
    code_name = 'Shop_Not_Found'
    message = 'shop not found.'
    zh_message = '店铺没有找到.'


class ErrorShopStateUnavailable(ApiError):
    """
    店铺状态不可用
    """
    code = 414004
    code_name = 'Shop_State_Unavailable'
    message = 'shop state unavailable.'
    zh_message = '店铺状态错误.'


# 授权类错误415xxx
class ErrorAccessTokenInvalid(ApiError):
    """
    无效token或token已过期
    """
    code = 415001
    code_name = 'Invalid_Access_Token'
    message = 'Access token invalid, expired or not exists.'
    status = HTTP_FORBIDDEN
    zh_message = '无效token或token已过期.'


class ErrorRequestTokenInvalid(ApiError):
    code = 415002
    code_name = 'Invalid_Requst_Token'
    message = 'Request token invalid, expired or not exists.'
    status = HTTP_FORBIDDEN
    zh_message = ''


class ErrorRefreshTokenInvalid(ApiError):
    code = 415003
    code_name = 'Invalid_Refresh_Token'
    message = 'Refresh token invalid, refresh access-token failed.'
    status = HTTP_FORBIDDEN
    zh_message = ''


class ErrorRequestTokenCreateFailed(ApiError):
    """
    Request Token创建失败
    """
    code = 415004
    code_name = 'Request_Token_Create_Failed'
    message = 'request token create failed.'
    zh_message = 'Request Token创建失败.'


class ErrorQrcodeTokenCreateFailed(ApiError):
    """
    Qrcode Token创建失败
    """
    code = 415005
    code_name = 'Qrcode_Token_Create_Failed'
    message = 'qrcode token create failed.'
    zh_message = 'Qrcode Token创建失败.'


class ErrorQrcodeTokenNotFound(ApiError):
    """
    Qrcode Token没有找到
    """
    code = 415006
    code_name = 'Qrcode_Token_not_Found'
    message = 'qrcode token not found.'
    zh_message = 'Qrcode Token没有找到.'


class ErrorQrcodeTokenExpired(ApiError):
    """

    """
    code = 415007
    code_name = 'Qrcode_Token_Expired'
    message = 'qrcode token expired.'
    zh_message = 'Qrcode Token失效.'


class ErrorQrcodeTokenError(ApiError):
    """
    Qrcode Token错误
    """
    code = 415008
    code_name = 'Qrcode_Token_Error'
    message = 'qrcode token error.'
    zh_message = 'Qrcode Token错误.'


class ErrorExChangeAccessTokenError(ApiError):
    """
    交换Access Token错误
    """
    code = 415009
    code_name = 'ExChange_Access_Token_Error'
    message = 'exchange access token error.'
    zh_message = '交换Access Token错误.'


# 工具类错误416xxx
class ErrorSendSmsFailed(ApiError):
    """
    发送验证码失败
    """
    code = 416001
    code_name = 'Send_Sms_Failed'
    message = 'send sms failed.'
    zh_message = '发送验证码失败.'


class ErrorQiniuCreateTokenFailed(ApiError):
    """
    创建七牛Token失败
    """
    code = 416002
    code_name = 'Qiniu_Create_Token_Failed'
    message = 'qiniu create token failed.'
    zh_message = '创建七牛Token失败.'


# 审核类错误417XXX
class ErrorApprovedFailed(ApiError):
    """
    审核失败
    """
    code = 417001
    code_name = 'Approved_Failed'
    message = 'approved failed.'
    zh_message = '审核失败.'


class ErrorApplyVerifyFailed(ApiError):
    """
    提交审核失败
    """
    code = 417002
    code_name = 'Apply_Verify_Failed'
    message = 'apply verify failed.'
    zh_message = '提交审核失败.'


class ErrorApplyNotFound(ApiError):
    """
    审核记录没有找到
    """
    code = 417003
    code_name = 'Apply_Not_Found'
    message = 'apply not found.'
    zh_message = '审核记录没有找到.'


# 权限类错误418xxx
class ErrorNotPermission(ApiError):
    """
    无权限操作
    """
    code = 418001
    code_name = 'Not_Permission'
    message = 'not permission.'
    zh_message = '无权限操作.'


class ErrorMethodPermissionConfigError(ApiError):
    """
    接口权限配置错误
    """
    code = 418002
    code_name = 'Method_Permission_Config_Error'
    message = 'method permission config error.'
    zh_message = '接口权限配置错误.'


class ErrorPermissionStateError(ApiError):
    """
    权限状态不可用
    """
    code = 418003
    code_name = 'Method_Permission_Config_Error'
    message = 'method permission config error.'
    zh_message = '权限状态不可用.'


# 钱包类错误419xxx
class ErrorPayChannelNotSupport(ApiError):
    """
    充值渠道不支持
    """
    code = 419001
    code_name = 'Pay_Channel_Not_Support'
    message = 'pay channel not support.'
    zh_message = '充值渠道不支持.'


class ErrorWalletRechargeCreateFailed(ApiError):
    """
    充值单创建失败
    """
    code = 419002
    code_name = 'Wallet_Recharge_Create_Failed'
    message = 'wallet recharge create failed.'
    zh_message = '充值单创建失败.'


class ErrorWalletNotFound(ApiError):
    """
    钱包没有找到
    """
    code = 419003
    code_name = 'Wallet_Not_Found'
    message = 'wallet not found.'
    zh_message = '钱包没有找到.'


class ErrorWalletState(ApiError):
    """
    钱包状态错误
    """
    code = 419004
    code_name = 'Wallet_State_Error'
    message = 'wallet state error.'
    zh_message = '钱包状态错误.'


class ErrorWalletAmountLess(ApiError):
    """
    钱包金额不足
    """
    code = 419005
    code_name = 'Wallet_Amount_Less'
    message = 'wallet amount less.'
    zh_message = '钱包金额不足.'


# 其他错误499xxx
class ErrorUnknownError(ApiError):
    """
    未知异常
    """
    code = 499999
    code_name = 'Unknown_Error'
    message = 'unknown error.'
    zh_message = '未知异常.'


# 系统类错误
class ErrorInternalSystem(ApiError):
    """
    系统错误
    """
    code = 500100
    code_name = 'System_Error'
    message = 'internal system error.'
    zh_message = '系统错误.'


class ErrorSystemConfigError(ApiError):
    """
    系统配置错误
    """
    code = 500101
    code_name = 'System_Config_Error'
    message = 'system config error.'
    zh_message = '系统配置错误.'

class ErrorRPCError(ApiError):
    """
    RPC错误
    """
    code = 500200
    code_name = 'Rpc_Error'
    message = 'rpc error.'
    zh_message = 'PRC错误.'


# 签名类错误6XX
class ErrorSignError(ApiError):
    """
    验签失败
    """
    code = 600101
    code_name = 'Sign_Error'
    message = 'sign error.'
    zh_message = '签名错误.'


class ErrorResourceNotFound(ApiError):
    code = 1000
    code_name = 'ResourceNotFound'
    status = HTTP_NOT_FOUND

    def __init__(self, object_id=None, *args, **kwargs):
        if object_id:
            self.message = 'Resource:[by id:%s] not found.' % object_id
        super(ErrorResourceNotFound, self).__init__(*args, **kwargs)


class ErrorObjectIdInvalid(ApiError):
    code = 1001
    code_name = 'ObjectIdInvalid'
    message = 'object id is missing or invalid.'


class ErrorValidateFailed(ApiError):
    code = 1002
    code_name = 'OperationValidateFailed'
    message = 'Request params validation failed'


class ErrorObjectStateInvalid(ApiError):
    code = 1004
    code_name = 'ObjectStateInvalid'
    message = 'object state not valid for this operation'

    def __init__(self, object_name=None, *args, **kwargs):
        if object_name:
            self.message = '%s state not valid for this operation' % object_name
        super(ErrorObjectStateInvalid, self).__init__(*args, **kwargs)


# 团队类错误420xxx
class ErrorTeamCreateFailed(ApiError):
    """
    团队创建失败
    """
    code = 420001
    code_name = 'Team_Create_Failed'
    message = 'Team create failed.'
    zh_message = '团队创建失败.'


class ErrorTeamUpdateFailed(ApiError):
    """
    团队更新失败
    """
    code = 420002
    code_name = 'Team_Update_Failed'
    message = 'Team update failed.'
    zh_message = '团队更新失败.'


class ErrorTeamNotFound(ApiError):
    """
    团队没有找到
    """
    code = 420003
    code_name = 'Team_not_found'
    message = 'team not found.'
    zh_message = '团队没有找到.'


# 供应商类错误421xxx
class ErrorVendorBizInfoCreateFailed(ApiError):
    """
    供应商信息创建失败
    """
    code = 421001
    code_name = 'Vendor_Biz_Info_Create_Failed'
    message = 'vendor biz info create failed.'
    zh_message = '供应商信息创建失败.'


class ErrorVendorBizInfoUpdateFailed(ApiError):
    """
    供应商信息更新错误
    """
    code = 421002
    code_name = 'Vendor_Biz_Info_Update_Failed'
    message = 'vendor biz info update failed.'
    zh_message = '供应商信息更新错误.'


class ErrorVendorBizInfoNotFound(ApiError):
    """
    供应商信息没有找到
    """
    code = 421003
    code_name = 'Vendor_Biz_Info_Not_Found'
    message = 'vendor biz info not found.'
    zh_message = '供应商信息没有找到.'


class ErrorVendorBizInfoAlreadyExist(ApiError):
    """
    供应商信息已存在
    """
    code = 421004
    code_name = 'Vendor_Biz_Info_Already_Exist'
    message = 'vendor biz info already exist.'
    zh_message = '供应商信息已存在.'


class ErrorVendorBizInfoActiveFailed(ApiError):
    """
    开启业务失败
    """
    code = 421005
    code_name = 'Vendor_Biz_Info_Active_Failed'
    message = 'vendor biz info active failed.'
    zh_message = '开启业务失败.'


class ErrorVendorBizInfoBannedFailed(ApiError):
    """
    关闭业务失败
    """
    code = 421006
    code_name = 'Vendor_Biz_Info_Banned_Failed'
    message = 'vendor biz info banned failed.'
    zh_message = '关闭业务失败.'


class ErrorCannotBeYourSelf(ApiError):
    """
    不能添加本人账户为承运商
    """
    code = 421007
    code_name = 'ErrorCannotBeYourSelf'
    message = 'ErrorCannotBeYourSelf'
    zh_message = '不能添加本人.'


# 分单规则类接口422xxx
class ErrorDeliveryDispatchRuleAlreadyExist(ApiError):
    """
    运力分单规则已存在
    """
    code = 422001
    code_name = 'Delivery_Dispatch_Rule_Already_Exist'
    message = 'delivery dispatch rule already exist.'
    zh_message = '运力分单规则已存在.'


class ErrorDeliveryDispatchRuleNotFound(ApiError):
    """
    运力分单规则没有找到
    """
    code = 422002
    code_name = 'Delivery_Dispatch_Rule_Not_Found'
    message = 'delivery dispatch rule not found.'
    zh_message = '运力分单规则没有找到.'


class ErrorDeliveryDispatchRuleCreateFailed(ApiError):
    """
    运力分单规则创建失败
    """
    code = 422003
    code_name = 'Delivery_Dispatch_Rule_Create_Failed'
    message = 'delivery dispatch rule create failed.'
    zh_message = '运力分单规则创建失败.'


class ErrorDeliveryDispatchRuleUpdateFailed(ApiError):
    """
    运力分单规则更新失败
    """
    code = 422004
    code_name = 'Delivery_Dispatch_Rule_Update_Failed'
    message = 'delivery dispatch rule update failed.'
    zh_message = '运力分单规则更新失败.'


class ErrorDeliveryDispatchRuleState(ApiError):
    """
    运力分单规则状态错误
    """
    code = 422005
    code_name = 'Delivery_Dispatch_Rule_State_Error'
    message = 'delivery dispatch rule state error.'
    zh_message = '运力分单规则状态错误.'


class ErrorDeliveryDispatchRulePublishFailed(ApiError):
    """
    运力分单规则发布失败
    """
    code = 422006
    code_name = 'Delivery_Dispatch_Rule_Publish_Failed'
    message = 'delivery dispatch rule publish failed.'
    zh_message = '运力分单规则发布失败.'


class ErrorCourierDispatchRuleAlreadyExist(ApiError):
    """
    骑士分单规则已存在
    """
    code = 422007
    code_name = 'Courier_Dispatch_Rule_Already_Exist'
    message = 'courier dispatch rule already exist.'
    zh_message = '骑士分单规则已存在.'


class ErrorCourierDispatchRuleNotFound(ApiError):
    """
    骑士分单规则没有找到
    """
    code = 422008
    code_name = 'Courier_Dispatch_Rule_Not_Found'
    message = 'courier dispatch rule not found.'
    zh_message = '骑士分单规则没有找到.'


class ErrorCourierDispatchRuleCreateFailed(ApiError):
    """
    骑士分单规则创建失败
    """
    code = 422009
    code_name = 'Courier_Dispatch_Rule_Create_Failed'
    message = 'courier dispatch rule create failed.'
    zh_message = '骑士分单规则创建失败.'


class ErrorCourierDispatchRuleUpdateFailed(ApiError):
    """
    骑士分单规则更新失败
    """
    code = 422010
    code_name = 'Courier_Dispatch_Rule_Update_Failed'
    message = 'courier dispatch rule update failed.'
    zh_message = '骑士分单规则更新失败.'


class ErrorCourierDispatchRuleState(ApiError):
    """
    骑士分单规则状态错误
    """
    code = 422011
    code_name = 'Courier_Dispatch_Rule_State_Error'
    message = 'courier dispatch rule state error.'
    zh_message = '骑士分单规则状态错误.'


class ErrorCourierDispatchRulePublishFailed(ApiError):
    """
    骑士分单规则发布失败
    """
    code = 422012
    code_name = 'Courier_Dispatch_Rule_Publish_Failed'
    message = 'courier dispatch rule publish failed.'
    zh_message = '骑士分单规则发布失败.'


class ErrorRulePriorityAlreadyExist(ApiError):
    """
    分单规则的优先级已存在
    """
    code = 422013
    code_name = 'Rule_Priority_Already_Exist'
    message = 'rule priority already exist.'
    zh_message = '分单规则的优先级已存在.'


class ErrorDisableRuleFailed(ApiError):
    """
    禁用分单规则失败
    """
    code = 422014
    code_name = 'Disable_Rule_Failed'
    message = 'disable rule failed.'
    zh_message = '禁用分单规则失败.'


class ErrorExistUsedRules(ApiError):
    """
    存在正在使用的分单规则
    """
    code = 422015
    code_name = 'Exist_Used_Rules'
    message = 'exist used rules'
    zh_message = '存在正在使用的分单规则.'


# 区域合作类接口423xxx
class ErrorVendorBizAreaAlreadyExist(ApiError):
    """
    区域合作已存在
    """
    code = 423001
    code_name = 'Vendor_Biz_Area_Already_Exist'
    message = 'vendor biz area already exist.'
    zh_message = '区域合作已存在.'


class ErrorVendorBizAreaNotFound(ApiError):
    """
    区域合作没有找到
    """
    code = 423002
    code_name = 'Vendor_Biz_Area_Not_Found'
    message = 'vendor biz area not found.'
    zh_message = '区域合作没有找到.'


class ErrorVendorBizAreaCreateFailed(ApiError):
    """
    区域合作创建失败
    """
    code = 423003
    code_name = 'Vendor_Biz_Area_Create_Failed'
    message = 'vendor biz area create failed.'
    zh_message = '区域合作创建失败.'


class ErrorVendorBizAreaUpdateFailed(ApiError):
    """
    区域合作更新失败
    """
    code = 423004
    code_name = 'Vendor_Biz_Area_Update_Failed'
    message = 'vendor biz area update failed.'
    zh_message = '区域合作更新失败.'


class ErrorVendorBizAreaState(ApiError):
    """
    区域合作状态错误
    """
    code = 423005
    code_name = 'Vendor_Biz_Area_State_Error'
    message = 'vendor biz area state error.'
    zh_message = '区域合作状态错误.'


# 分单记录类接口424xxx
class ErrorVendorOrderNotFound(ApiError):
    """
    分单记录没有找到
    """
    code = 424002
    code_name = 'Vendor_Order_Not_Found'
    message = 'vendor order not found.'
    zh_message = '分单记录没有找到.'


# 结算规则类接口425xxx
class ErrorCourierPriceRuleAlreadyExist(ApiError):
    """
    骑士结算规则已存在
    """
    code = 425001
    code_name = 'Courier_Price_Rule_Already_Exist'
    message = 'courier price rule already exist.'
    zh_message = '骑士结算规则已存在.'


class ErrorCourierPriceRuleNotFound(ApiError):
    """
    骑士结算规则没有找到
    """
    code = 425002
    code_name = 'Courier_Price_Rule_Not_Found'
    message = 'courier price rule not found.'
    zh_message = '骑士结算规则没有找到.'


class ErrorCourierPriceRuleCreateFailed(ApiError):
    """
    骑士结算规则创建失败
    """
    code = 425003
    code_name = 'Courier_Price_Rule_Create_Failed'
    message = 'courier price rule create failed.'
    zh_message = '骑士结算规则创建失败.'


class ErrorCourierPriceRuleUpdateFailed(ApiError):
    """
    骑士结算规则更新失败
    """
    code = 425004
    code_name = 'Courier_Price_Rule_Update_Failed'
    message = 'courier price rule update failed.'
    zh_message = '骑士结算规则更新失败.'


class ErrorCourierPriceRuleState(ApiError):
    """
    骑士结算规则状态错误
    """
    code = 425005
    code_name = 'Courier_Price_Rule_State_Error'
    message = 'courier price rule state error.'
    zh_message = '骑士结算规则状态错误.'


class ErrorCourierPriceRulePublishFailed(ApiError):
    """
    骑士结算规则发布失败
    """
    code = 425006
    code_name = 'Courier_Price_Rule_Publish_Failed'
    message = 'courier price rule publish failed.'
    zh_message = '骑士结算规则发布失败.'


class ErrorVendorPriceRuleAlreadyExist(ApiError):
    """
    服务商结算规则已存在
    """
    code = 425007
    code_name = 'Vendor_Price_Rule_Already_Exist'
    message = 'vendor price rule already exist.'
    zh_message = '服务商结算规则已存在.'


class ErrorVendorPriceRuleNotFound(ApiError):
    """
    服务商结算规则没有找到
    """
    code = 425008
    code_name = 'Vendor_Price_Rule_Not_Found'
    message = 'vendor price rule not found.'
    zh_message = '服务商结算规则没有找到.'


class ErrorVendorPriceRuleCreateFailed(ApiError):
    """
    服务商结算规则创建失败
    """
    code = 425009
    code_name = 'Vendor_Price_Rule_Create_Failed'
    message = 'vendor price rule create failed.'
    zh_message = '服务商结算规则创建失败.'


class ErrorVendorPriceRuleUpdateFailed(ApiError):
    """
    服务商结算规则更新失败
    """
    code = 425010
    code_name = 'Vendor_Price_Rule_Update_Failed'
    message = 'vendor price rule update failed.'
    zh_message = '服务商结算规则更新失败.'


class ErrorVendorPriceRuleState(ApiError):
    """
    服务商结算规则状态错误
    """
    code = 425011
    code_name = 'Vendor_Price_Rule_State_Error'
    message = 'vendor price rule state error.'
    zh_message = '服务商结算规则状态错误.'


class ErrorVendorPriceRulePublishFailed(ApiError):
    """
    服务商结算规则发布失败
    """
    code = 425012
    code_name = 'Vendor_Price_Rule_Publish_Failed'
    message = 'vendor price rule publish failed.'
    zh_message = '服务商结算规则发布失败.'


class ErrorRegionHitRuleNotFound(ApiError):
    """
    判区规则没有找到
    """
    code = 426001
    code_name = 'Region_Hit_Rule_Not_Found'
    message = 'region hit rule not found.'
    zh_message = '判区规则没有找到.'


class ErrorRegionHitRuleStateError(ApiError):
    """
    判区规则状态错误
    """
    code = 426002
    code_name = 'Region_Hit_Rule_State_Error'
    message = 'region hit rule state error.'
    zh_message = '判区规则状态错误.'


class ErrorRegionHitRulePublishFailed(ApiError):
    """
    判区规则发布失败
    """
    code = 426003
    code_name = 'Region_Hit_Rule_Publish_Failed'
    message = 'region hit rule publish failed.'
    zh_message = '判区规则发布失败.'


class ErrorRegionHitRuleCreateFailed(ApiError):
    """
    判区规则创建失败
    """
    code = 426004
    code_name = 'Region_Hit_Rule_Create_Failed'
    message = 'region hit rule create failed.'
    zh_message = '判区规则创建失败.'


class ErrorRegionHitRuleAlreadyExist(ApiError):
    """
    判区规则已存在
    """
    code = 426005
    code_name = 'Region_Hit_Rule_AlreadyExist'
    message = 'region hit rule alreadyExist.'
    zh_message = '判区规则已存在.'


class ErrorRegionHitRuleUpdateFailed(ApiError):
    """
    判区规则更新失败
    """
    code = 426006
    code_name = 'Region_Hit_Rule_Update_Failed'
    message = 'region hit rule update failed.'
    zh_message = '判区规则更新失败.'


class ErrorSopNotFound(ApiError):
    """
    标准规则没有找到
    """
    code = 427001
    code_name = 'Sop_Not_Found'
    message = 'sop not found.'
    zh_message = '标准规则没有找到.'


class ErrorSopStateError(ApiError):
    """
    标准规则状态错误
    """
    code = 427002
    code_name = 'Sop_State_Error'
    message = 'sop state error.'
    zh_message = '标准规则状态错误.'


class ErrorSopPublishFailed(ApiError):
    """
    标准规则发布失败
    """
    code = 427003
    code_name = 'Sop_Publish_Failed'
    message = 'sop publish failed.'
    zh_message = '标准规则发布失败.'


class ErrorSopAlreadyExist(ApiError):
    """
    标准规则已存在
    """
    code = 427004
    code_name = 'Sop_AlreadyExist'
    message = 'sop alreadyExist.'
    zh_message = '标准规则已存在.'


class ErrorSopCreatedFailed(ApiError):
    """
    标准规则创建失败
    """
    code = 427005
    code_name = 'Sop_Created_Failed'
    message = 'sop created failed.'
    zh_message = '标准规则创建失败.'


class ErrorSopUpdateFailed(ApiError):
    """
    标准规则更新失败
    """
    code = 427006
    code_name = 'Sop_Update_Failed'
    message = 'sop update failed.'
    zh_message = '标准规则更新失败.'


class ErrorDevelopAlreadyExist(ApiError):
    """
    开发者信息已存在
    """
    code = 428001
    code_name = 'Develop_Already_Exist'
    message = 'develop already exist.'
    zh_message = '开发者信息已存在.'


class ErrorDevelopCreateFailed(ApiError):
    """
    开发者信息创建失败
    """
    code = 428002
    code_name = 'Develop_Create_Failed'
    message = 'develop create failed.'
    zh_message = '开发者信息创建失败.'


class ErrorDevelopUpdateFailed(ApiError):
    """
    开发者信息更新失败
    """
    code = 428003
    code_name = 'Develop_Update_Failed'
    message = 'develop update failed.'
    zh_message = '开发者信息更新失败.'


class ErrorDevelopNotFound(ApiError):
    """
    开发者信息没有找到
    """
    code = 428004
    code_name = 'Develop_Not_Found'
    message = 'develop not found.'
    zh_message = '开发者信息没有找到.'


class ErrorXinYiSystemError(ApiError):
    """
    芯易系统环境错误
    """
    code = 1000
    code_name = 'XinYi_System_Error'
    message = '系统内部错误'
    zh_message = '系统内部错误.'


class ErrorXinYiSignError(ApiError):
    """
    芯易签名错误
    """
    code = 1001
    code_name = 'XinYi_Sign_Error'
    message = '签名错误'
    zh_message = '签名错误.'


class ErrorXinYiArgumentInvalidError(ApiError):
    """
    芯易参数传递错误
    """
    code = 1002
    code_name = 'XinYi_Argument_Invalid_Error'
    message = '参数传递错误'
    zh_message = '参数传递错误.'


class ErrorXinYiAppidNotFound(ApiError):
    """
    芯易appid错误
    """
    code = 1003
    code_name = 'XinYi_Appid_Not_Found'
    message = 'appid错误'
    zh_message = 'appid错误.'


class ErrorXinYiRequestMethodError(ApiError):
    """
    芯易请求的命令方法错误
    """
    code = 1004
    code_name = 'XinYi_Request_Method_Error'
    message = '请求的命令方法错误'
    zh_message = '请求的命令方法错误.'


class ErrorXinYiParamsNotFound(ApiError):
    """
    芯易请求数据不存在
    """
    code = 1005
    code_name = 'XinYi_Params_Not_Found'
    message = '请求数据不存在'
    zh_message = '请求数据不存在.'


class ErrorDslConfigNotFound(ApiError):
    """
    DSL配置信息没有找到
    """
    code = 429001
    code_name = 'Dsl_Config_Not_Found'
    message = 'dsl config not found.'
    zh_message = 'DSL 配置错误.'


# 仓库类错误（430XXX）
class ErrorStockNotFound(ApiError):
    """
    仓库没有找到
    """
    code = 430001
    code_name = 'Stock_Not_Found'
    message = 'stock not found.'
    zh_message = '仓库没有找到.'


class ErrorStockNameExist(ApiError):
    """
    仓库名称已存在
    """
    code = 430002
    code_name = 'Stock_Name_Exist'
    message = 'stock name exist.'
    zh_message = '仓库名称已存在.'


class ErrorStockAreaRuleExist(ApiError):
    """
    仓库已关联区域
    """
    code = 430003
    code_name = 'Stock_Area_Rule_Exist'
    message = 'stock area rule exist.'
    zh_message = '仓库已关联区域.'


class ErrorStockHasDispatchRule(ApiError):
    """
    仓库有分单规则，无法禁用
    """
    code = 430004
    code_name = 'Stock_Has_Dispatch_Rule'
    message = 'stock has dispatch rule.'
    zh_message = '仓库有分单规则，无法禁用.'


class ErrorStockHasUndoneOrders(ApiError):
    """
    仓库有未完成仓库单，无法禁用
    """
    code = 430005
    code_name = 'Stock_Has_Undone_Orders'
    message = 'stock has undone orders.'
    zh_message = '仓库有未完成仓库单，无法禁用.'


# 仓库类错误（431XXX）
class ErrorStockDispatchRuleNotFound(ApiError):
    """
    仓库分单规则没有找到
    """
    code = 431001
    code_name = 'Stock_Dispatch_Rule_Not_Found'
    message = 'stock dispatch rule not found.'
    zh_message = '仓库分单规则没有找到.'


class ErrorStockDispatchRuleExist(ApiError):
    """
    仓库分单规则已存在
    """
    code = 431002
    code_name = 'Stock_Dispatch_Rule_Exist'
    message = 'stock dispatch rule exist.'
    zh_message = '仓库分单规则已存在.'


# 仓库订单类错误（432XXX）
class ErrorStockOrderNotFound(ApiError):
    """
    仓库订单没有找到
    """
    code = 432001
    code_name = 'Stock_Order_Not_Found'
    message = 'stock order not found.'
    zh_message = '仓库订单没有找到.'



ERROR_INVALID_ARGUMENT_CODE = 100
ERROR_RESOURCE_NOT_FOUND_CODE = 1000
ERROR_OBJECT_ID_INVALID_CODE = 1001
ERROR_VALIDATE_FAILED_CODE = 1002
ERROR_OBJECT_STATE_INVALID = 1004

ERROR_EXCHANGE_ACCESS_TOKEN_FAILED = 10404
ERROR_QRCODE_TOKEN_NOT_FOUND = 10406
ERROR_QRCODE_TOKEN_ERROR = 10407
ERROR_QRCODE_TOKEN_EXPIRED = 10408

CODE_MAPPING = {
    ERROR_INVALID_ARGUMENT_CODE: ErrorInvalidArgument,
    ERROR_RESOURCE_NOT_FOUND_CODE: ErrorResourceNotFound,
    ERROR_OBJECT_ID_INVALID_CODE: ErrorObjectIdInvalid,
    ERROR_VALIDATE_FAILED_CODE: ErrorValidateFailed,
    ERROR_OBJECT_STATE_INVALID: ErrorObjectStateInvalid,
    ERROR_QRCODE_TOKEN_NOT_FOUND: ErrorQrcodeTokenNotFound,
    ERROR_QRCODE_TOKEN_EXPIRED: ErrorQrcodeTokenExpired,
    ERROR_QRCODE_TOKEN_ERROR: ErrorQrcodeTokenError,
    ERROR_EXCHANGE_ACCESS_TOKEN_FAILED: ErrorExChangeAccessTokenError
}


def cast_api_error(ex):
    """Cast ApiError to its child instance, according its code
    :param ex:
    :type ex:
    :return:
    :rtype:
    """
    if not isinstance(ex, ApiError):
        return ex
    code = ex.code
    ex_cls = CODE_MAPPING.get(code)
    if not ex_cls:
        return ex
    ex.__class__ = ex_cls
    return ex


zh_message_control = {
    '401001': '参数缺失或错误.',
    '401007': '订单已存在.',
    '401010': '获取地址经纬度失败.',
    '401011': '地址超出配送范围.',
    '402003': '服务商没有找到.',
    '402004': '服务商不可用（状态错误）.',
    '402005': '服务商未审核通过.',
    '402006': '不在配送时间内.',
    '402007': '服务商状态错误.',
    '403003': '商户没有找到.',
    '403004': '商户被禁用.',
    '403005': '商户未审核通过.',
    '403006': '商户未签约.',
    '403007': '商户签约失败.',
    '403011': '未找到签约记录.',
    '403012': '签约记录状态错误.',
    '404003': '区域没有找到.',
    '404004': '区域状态错误.',
    '404009': '区域围栏没有找到.',
    '405003': '产品没有找到.',
    '405004': '产品不可用.',
    '405008': '产品版本没有找到.',
    '405006': '产品状态错误.',
    '409003': '骑士没有找到.',
    '409004': '骑士状态错误.',
    '409005': '骑士审核状态错误.',
    '410001': '订单发单失败.',
    '410002': '订单没有找到.',
    '410003': '订单状态错误.',
    '410004': '订单不允许关闭.',
    '410005': '订单关闭失败.',
    '410006': '订单不可催单.',
    '410007': '订单催单失败.',
    '410018': '订单催单时间错误.',
    '410008': '订单配送费估算失败.',
    '410009': '订单收货地址超出配送区域.',
    '410010': '订单收货地址判区失败.',
    '410011': '订单发货地址超出配送区域.',
    '410012': '订单发货地址判区失败.',
    '410013': '订单配送距离计算失败.',
    '410014': '订单超出配送区域.',
    '410017': '订单超出最大配送距离.',
    '414003': '店铺没有找到.',
    '414004': '店铺状态错误.',
    '419003': '钱包没有找到.',
    '419004': '钱包状态错误.',
    '419005': '钱包金额不足.',
    '499999': '未知异常.',
    '500100': '系统错误.',
    '500101': '系统配置错误.',
    '500200': 'PRC错误.',
    '600101': '签名错误.',
    '426001': '判区规则没有找到.',
    '426002': '判区规则状态错误.',
    '426003': '判区规则发布失败.',
    '430001': '仓库没有找到.',
    '431001': '仓库分单规则没有找到.',
}
