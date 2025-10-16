# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll111ll_opy_
from browserstack_sdk.bstack11l11l11_opy_ import bstack1llll1l11_opy_
def _11l1ll1l1ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1lll1111_opy_:
    def __init__(self, handler):
        self._11l1ll1l11l_opy_ = {}
        self._11l1ll1l1l1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llll1l11_opy_.version()
        if bstack11l1ll111ll_opy_(pytest_version, bstack1ll1ll1_opy_ (u"ࠦ࠽࠴࠱࠯࠳ࠥ᝺")) >= 0:
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝻")] = Module._register_setup_function_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝼")] = Module._register_setup_module_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝽")] = Class._register_setup_class_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝾")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝿"))
            Module._register_setup_module_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫក"))
            Class._register_setup_class_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫខ"))
            Class._register_setup_method_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭គ"))
        else:
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឃ")] = Module._inject_setup_function_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨង")] = Module._inject_setup_module_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨច")] = Class._inject_setup_class_fixture
            self._11l1ll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឆ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ជ"))
            Module._inject_setup_module_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឈ"))
            Class._inject_setup_class_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬញ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll11ll1_opy_(bstack1ll1ll1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧដ"))
    def bstack11l1ll1llll_opy_(self, bstack11l1ll1ll1l_opy_, hook_type):
        bstack11l1ll1111l_opy_ = id(bstack11l1ll1ll1l_opy_.__class__)
        if (bstack11l1ll1111l_opy_, hook_type) in self._11l1ll1l1l1_opy_:
            return
        meth = getattr(bstack11l1ll1ll1l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll1l1l1_opy_[(bstack11l1ll1111l_opy_, hook_type)] = meth
            setattr(bstack11l1ll1ll1l_opy_, hook_type, self.bstack11l1ll1l111_opy_(hook_type, bstack11l1ll1111l_opy_))
    def bstack11l1ll111l1_opy_(self, instance, bstack11l1ll11l11_opy_):
        if bstack11l1ll11l11_opy_ == bstack1ll1ll1_opy_ (u"ࠢࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឋ"):
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤឌ"))
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨឍ"))
        if bstack11l1ll11l11_opy_ == bstack1ll1ll1_opy_ (u"ࠥࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠦណ"):
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠥត"))
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠢថ"))
        if bstack11l1ll11l11_opy_ == bstack1ll1ll1_opy_ (u"ࠨࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࠨទ"):
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠧធ"))
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠤន"))
        if bstack11l1ll11l11_opy_ == bstack1ll1ll1_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠥប"):
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠤផ"))
            self.bstack11l1ll1llll_opy_(instance.obj, bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩࠨព"))
    @staticmethod
    def bstack11l1ll11111_opy_(hook_type, func, args):
        if hook_type in [bstack1ll1ll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫភ"), bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨម")]:
            _11l1ll1l1ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll1l111_opy_(self, hook_type, bstack11l1ll1111l_opy_):
        def bstack11l1ll1ll11_opy_(arg=None):
            self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧយ"))
            result = None
            try:
                bstack1l11111l1l1_opy_ = self._11l1ll1l1l1_opy_[(bstack11l1ll1111l_opy_, hook_type)]
                self.bstack11l1ll11111_opy_(hook_type, bstack1l11111l1l1_opy_, (arg,))
                result = Result(result=bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨរ"))
            except Exception as e:
                result = Result(result=bstack1ll1ll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩល"), exception=e)
                self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩវ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪឝ"), result)
        def bstack11l1ll1lll1_opy_(this, arg=None):
            self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬឞ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11111_opy_(hook_type, self._11l1ll1l1l1_opy_[hook_type], (this, arg))
                result = Result(result=bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ស"))
            except Exception as e:
                result = Result(result=bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧហ"), exception=e)
                self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧឡ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll1ll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨអ"), result)
        if hook_type in [bstack1ll1ll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩឣ"), bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឤ")]:
            return bstack11l1ll1lll1_opy_
        return bstack11l1ll1ll11_opy_
    def bstack11l1ll11ll1_opy_(self, bstack11l1ll11l11_opy_):
        def bstack11l1ll11l1l_opy_(this, *args, **kwargs):
            self.bstack11l1ll111l1_opy_(this, bstack11l1ll11l11_opy_)
            self._11l1ll1l11l_opy_[bstack11l1ll11l11_opy_](this, *args, **kwargs)
        return bstack11l1ll11l1l_opy_