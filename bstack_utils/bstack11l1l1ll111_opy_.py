# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l1ll1ll_opy_
from browserstack_sdk.bstack1llllllll_opy_ import bstack1lll111l1_opy_
def _11l1l1lll1l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll111l1_opy_:
    def __init__(self, handler):
        self._11l1ll11111_opy_ = {}
        self._11l1l1l1l11_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1lll111l1_opy_.version()
        if bstack11l1l1ll1ll_opy_(pytest_version, bstack1l111ll_opy_ (u"ࠥ࠼࠳࠷࠮࠲ࠤផ")) >= 0:
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧព")] = Module._register_setup_function_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ភ")] = Module._register_setup_module_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ម")] = Class._register_setup_class_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨយ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫរ"))
            Module._register_setup_module_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪល"))
            Class._register_setup_class_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪវ"))
            Class._register_setup_method_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឝ"))
        else:
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឞ")] = Module._inject_setup_function_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧស")] = Module._inject_setup_module_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧហ")] = Class._inject_setup_class_fixture
            self._11l1ll11111_opy_[bstack1l111ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឡ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬអ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឣ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឤ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1l1l1l_opy_(bstack1l111ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឥ"))
    def bstack11l1ll1111l_opy_(self, bstack11l1l1l1ll1_opy_, hook_type):
        bstack11l1l1ll11l_opy_ = id(bstack11l1l1l1ll1_opy_.__class__)
        if (bstack11l1l1ll11l_opy_, hook_type) in self._11l1l1l1l11_opy_:
            return
        meth = getattr(bstack11l1l1l1ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1l1l11_opy_[(bstack11l1l1ll11l_opy_, hook_type)] = meth
            setattr(bstack11l1l1l1ll1_opy_, hook_type, self.bstack11l1l1l11ll_opy_(hook_type, bstack11l1l1ll11l_opy_))
    def bstack11l1l1lll11_opy_(self, instance, bstack11l1l1llll1_opy_):
        if bstack11l1l1llll1_opy_ == bstack1l111ll_opy_ (u"ࠨࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឦ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣឧ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧឨ"))
        if bstack11l1l1llll1_opy_ == bstack1l111ll_opy_ (u"ࠤࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឩ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠤឪ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࠨឫ"))
        if bstack11l1l1llll1_opy_ == bstack1l111ll_opy_ (u"ࠧࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠧឬ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠦឭ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠣឮ"))
        if bstack11l1l1llll1_opy_ == bstack1l111ll_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឯ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠣឰ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1l111ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠧឱ"))
    @staticmethod
    def bstack11l1l1ll1l1_opy_(hook_type, func, args):
        if hook_type in [bstack1l111ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪឲ"), bstack1l111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧឳ")]:
            _11l1l1lll1l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1l11ll_opy_(self, hook_type, bstack11l1l1ll11l_opy_):
        def bstack11l1ll111ll_opy_(arg=None):
            self.handler(hook_type, bstack1l111ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭឴"))
            result = None
            try:
                bstack11llllll1ll_opy_ = self._11l1l1l1l11_opy_[(bstack11l1l1ll11l_opy_, hook_type)]
                self.bstack11l1l1ll1l1_opy_(hook_type, bstack11llllll1ll_opy_, (arg,))
                result = Result(result=bstack1l111ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ឵"))
            except Exception as e:
                result = Result(result=bstack1l111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨា"), exception=e)
                self.handler(hook_type, bstack1l111ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨិ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l111ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩី"), result)
        def bstack11l1l1l1lll_opy_(this, arg=None):
            self.handler(hook_type, bstack1l111ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫឹ"))
            result = None
            exception = None
            try:
                self.bstack11l1l1ll1l1_opy_(hook_type, self._11l1l1l1l11_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l111ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬឺ"))
            except Exception as e:
                result = Result(result=bstack1l111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ុ"), exception=e)
                self.handler(hook_type, bstack1l111ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ូ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l111ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧួ"), result)
        if hook_type in [bstack1l111ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨើ"), bstack1l111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬឿ")]:
            return bstack11l1l1l1lll_opy_
        return bstack11l1ll111ll_opy_
    def bstack11l1l1l1l1l_opy_(self, bstack11l1l1llll1_opy_):
        def bstack11l1l1lllll_opy_(this, *args, **kwargs):
            self.bstack11l1l1lll11_opy_(this, bstack11l1l1llll1_opy_)
            self._11l1ll11111_opy_[bstack11l1l1llll1_opy_](this, *args, **kwargs)
        return bstack11l1l1lllll_opy_