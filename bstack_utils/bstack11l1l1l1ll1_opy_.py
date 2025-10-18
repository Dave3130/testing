# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll11l1l_opy_
from browserstack_sdk.bstack1lll1ll1l_opy_ import bstack111lll11_opy_
def _11l1l1l1lll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll11111_opy_:
    def __init__(self, handler):
        self._11l1l1l1l1l_opy_ = {}
        self._11l1ll111ll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111lll11_opy_.version()
        if bstack11l1ll11l1l_opy_(pytest_version, bstack11l111_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢរ")) >= 0:
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬល")] = Module._register_setup_function_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫវ")] = Module._register_setup_module_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឝ")] = Class._register_setup_class_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឞ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩស"))
            Module._register_setup_module_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨហ"))
            Class._register_setup_class_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឡ"))
            Class._register_setup_method_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪអ"))
        else:
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឣ")] = Module._inject_setup_function_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឤ")] = Module._inject_setup_module_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឥ")] = Class._inject_setup_class_fixture
            self._11l1l1l1l1l_opy_[bstack11l111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឦ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឧ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឨ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឩ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឪ"))
    def bstack11l1ll1111l_opy_(self, bstack11l1l1ll11l_opy_, hook_type):
        bstack11l1l1ll1l1_opy_ = id(bstack11l1l1ll11l_opy_.__class__)
        if (bstack11l1l1ll1l1_opy_, hook_type) in self._11l1ll111ll_opy_:
            return
        meth = getattr(bstack11l1l1ll11l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll111ll_opy_[(bstack11l1l1ll1l1_opy_, hook_type)] = meth
            setattr(bstack11l1l1ll11l_opy_, hook_type, self.bstack11l1ll11l11_opy_(hook_type, bstack11l1l1ll1l1_opy_))
    def bstack11l1l1ll111_opy_(self, instance, bstack11l1l1lll1l_opy_):
        if bstack11l1l1lll1l_opy_ == bstack11l111_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢឫ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨឬ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥឭ"))
        if bstack11l1l1lll1l_opy_ == bstack11l111_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឮ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢឯ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦឰ"))
        if bstack11l1l1lll1l_opy_ == bstack11l111_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឱ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤឲ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨឳ"))
        if bstack11l1l1lll1l_opy_ == bstack11l111_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ឴"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨ឵"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack11l111_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥា"))
    @staticmethod
    def bstack11l1l1lllll_opy_(hook_type, func, args):
        if hook_type in [bstack11l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨិ"), bstack11l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬី")]:
            _11l1l1l1lll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll11l11_opy_(self, hook_type, bstack11l1l1ll1l1_opy_):
        def bstack11l1ll111l1_opy_(arg=None):
            self.handler(hook_type, bstack11l111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫឹ"))
            result = None
            try:
                bstack1l111111111_opy_ = self._11l1ll111ll_opy_[(bstack11l1l1ll1l1_opy_, hook_type)]
                self.bstack11l1l1lllll_opy_(hook_type, bstack1l111111111_opy_, (arg,))
                result = Result(result=bstack11l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬឺ"))
            except Exception as e:
                result = Result(result=bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ុ"), exception=e)
                self.handler(hook_type, bstack11l111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ូ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧួ"), result)
        def bstack11l1l1ll1ll_opy_(this, arg=None):
            self.handler(hook_type, bstack11l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩើ"))
            result = None
            exception = None
            try:
                self.bstack11l1l1lllll_opy_(hook_type, self._11l1ll111ll_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪឿ"))
            except Exception as e:
                result = Result(result=bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫៀ"), exception=e)
                self.handler(hook_type, bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫេ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬែ"), result)
        if hook_type in [bstack11l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ៃ"), bstack11l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪោ")]:
            return bstack11l1l1ll1ll_opy_
        return bstack11l1ll111l1_opy_
    def bstack11l1l1lll11_opy_(self, bstack11l1l1lll1l_opy_):
        def bstack11l1l1llll1_opy_(this, *args, **kwargs):
            self.bstack11l1l1ll111_opy_(this, bstack11l1l1lll1l_opy_)
            self._11l1l1l1l1l_opy_[bstack11l1l1lll1l_opy_](this, *args, **kwargs)
        return bstack11l1l1llll1_opy_