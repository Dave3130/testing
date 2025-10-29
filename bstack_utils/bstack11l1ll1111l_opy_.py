# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll11111_opy_
from browserstack_sdk.bstack11111ll1_opy_ import bstack1llll1lll_opy_
def _11l1l1l1l11_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1lllll_opy_:
    def __init__(self, handler):
        self._11l1l1ll1l1_opy_ = {}
        self._11l1l1ll1ll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llll1lll_opy_.version()
        if bstack11l1ll11111_opy_(pytest_version, bstack11l11ll_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨឧ")) >= 0:
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឨ")] = Module._register_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឩ")] = Module._register_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឪ")] = Class._register_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឫ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឬ"))
            Module._register_setup_module_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឭ"))
            Class._register_setup_class_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឮ"))
            Class._register_setup_method_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឯ"))
        else:
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឰ")] = Module._inject_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឱ")] = Module._inject_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឲ")] = Class._inject_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11l11ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឳ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ឴"))
            Module._inject_setup_module_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ឵"))
            Class._inject_setup_class_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨា"))
            Class._inject_setup_method_fixture = self.bstack11l1l1l1lll_opy_(bstack11l11ll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪិ"))
    def bstack11l1l1lll1l_opy_(self, bstack11l1l1l1ll1_opy_, hook_type):
        bstack11l1l1lll11_opy_ = id(bstack11l1l1l1ll1_opy_.__class__)
        if (bstack11l1l1lll11_opy_, hook_type) in self._11l1l1ll1ll_opy_:
            return
        meth = getattr(bstack11l1l1l1ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1ll1ll_opy_[(bstack11l1l1lll11_opy_, hook_type)] = meth
            setattr(bstack11l1l1l1ll1_opy_, hook_type, self.bstack11l1l1l11l1_opy_(hook_type, bstack11l1l1lll11_opy_))
    def bstack11l1l1l1l1l_opy_(self, instance, bstack11l1l1l111l_opy_):
        if bstack11l1l1l111l_opy_ == bstack11l11ll_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨី"):
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧឹ"))
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤឺ"))
        if bstack11l1l1l111l_opy_ == bstack11l11ll_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢុ"):
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨូ"))
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥួ"))
        if bstack11l1l1l111l_opy_ == bstack11l11ll_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤើ"):
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣឿ"))
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧៀ"))
        if bstack11l1l1l111l_opy_ == bstack11l11ll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨេ"):
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧែ"))
            self.bstack11l1l1lll1l_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤៃ"))
    @staticmethod
    def bstack11l1l1ll111_opy_(hook_type, func, args):
        if hook_type in [bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧោ"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫៅ")]:
            _11l1l1l1l11_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1l11l1_opy_(self, hook_type, bstack11l1l1lll11_opy_):
        def bstack11l1l1llll1_opy_(arg=None):
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪំ"))
            result = None
            try:
                bstack11llllll1ll_opy_ = self._11l1l1ll1ll_opy_[(bstack11l1l1lll11_opy_, hook_type)]
                self.bstack11l1l1ll111_opy_(hook_type, bstack11llllll1ll_opy_, (arg,))
                result = Result(result=bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫះ"))
            except Exception as e:
                result = Result(result=bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬៈ"), exception=e)
                self.handler(hook_type, bstack11l11ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ៉"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭៊"), result)
        def bstack11l1l1l11ll_opy_(this, arg=None):
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ់"))
            result = None
            exception = None
            try:
                self.bstack11l1l1ll111_opy_(hook_type, self._11l1l1ll1ll_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ៌"))
            except Exception as e:
                result = Result(result=bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ៍"), exception=e)
                self.handler(hook_type, bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪ៎"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ៏"), result)
        if hook_type in [bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬ័"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ៑")]:
            return bstack11l1l1l11ll_opy_
        return bstack11l1l1llll1_opy_
    def bstack11l1l1l1lll_opy_(self, bstack11l1l1l111l_opy_):
        def bstack11l1l1ll11l_opy_(this, *args, **kwargs):
            self.bstack11l1l1l1l1l_opy_(this, bstack11l1l1l111l_opy_)
            self._11l1l1ll1l1_opy_[bstack11l1l1l111l_opy_](this, *args, **kwargs)
        return bstack11l1l1ll11l_opy_