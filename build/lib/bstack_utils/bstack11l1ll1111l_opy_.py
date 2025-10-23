# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l1l1ll1_opy_
from browserstack_sdk.bstack11111l1l_opy_ import bstack1lllllll1_opy_
def _11l1l1lllll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1ll11l_opy_:
    def __init__(self, handler):
        self._11l1ll11l11_opy_ = {}
        self._11l1l1ll1l1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1lllllll1_opy_.version()
        if bstack11l1l1l1ll1_opy_(pytest_version, bstack11lll1_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣប")) >= 0:
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ផ")] = Module._register_setup_function_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬព")] = Module._register_setup_module_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬភ")] = Class._register_setup_class_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧម")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪយ"))
            Module._register_setup_module_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩរ"))
            Class._register_setup_class_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩល"))
            Class._register_setup_method_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫវ"))
        else:
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឝ")] = Module._inject_setup_function_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឞ")] = Module._inject_setup_module_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ស")] = Class._inject_setup_class_fixture
            self._11l1ll11l11_opy_[bstack11lll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨហ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឡ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪអ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឣ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1ll1ll_opy_(bstack11lll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឤ"))
    def bstack11l1l1l1lll_opy_(self, bstack11l1l1ll111_opy_, hook_type):
        bstack11l1ll111ll_opy_ = id(bstack11l1l1ll111_opy_.__class__)
        if (bstack11l1ll111ll_opy_, hook_type) in self._11l1l1ll1l1_opy_:
            return
        meth = getattr(bstack11l1l1ll111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1ll1l1_opy_[(bstack11l1ll111ll_opy_, hook_type)] = meth
            setattr(bstack11l1l1ll111_opy_, hook_type, self.bstack11l1l1l1l1l_opy_(hook_type, bstack11l1ll111ll_opy_))
    def bstack11l1l1llll1_opy_(self, instance, bstack11l1l1l1l11_opy_):
        if bstack11l1l1l1l11_opy_ == bstack11lll1_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឥ"):
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢឦ"))
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦឧ"))
        if bstack11l1l1l1l11_opy_ == bstack11lll1_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឨ"):
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣឩ"))
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧឪ"))
        if bstack11l1l1l1l11_opy_ == bstack11lll1_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦឫ"):
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥឬ"))
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢឭ"))
        if bstack11l1l1l1l11_opy_ == bstack11lll1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឮ"):
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢឯ"))
            self.bstack11l1l1l1lll_opy_(instance.obj, bstack11lll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦឰ"))
    @staticmethod
    def bstack11l1l1lll11_opy_(hook_type, func, args):
        if hook_type in [bstack11lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩឱ"), bstack11lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឲ")]:
            _11l1l1lllll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1l1l1l_opy_(self, hook_type, bstack11l1ll111ll_opy_):
        def bstack11l1l1lll1l_opy_(arg=None):
            self.handler(hook_type, bstack11lll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬឳ"))
            result = None
            try:
                bstack11llllll1ll_opy_ = self._11l1l1ll1l1_opy_[(bstack11l1ll111ll_opy_, hook_type)]
                self.bstack11l1l1lll11_opy_(hook_type, bstack11llllll1ll_opy_, (arg,))
                result = Result(result=bstack11lll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭឴"))
            except Exception as e:
                result = Result(result=bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ឵"), exception=e)
                self.handler(hook_type, bstack11lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧា"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨិ"), result)
        def bstack11l1ll11111_opy_(this, arg=None):
            self.handler(hook_type, bstack11lll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪី"))
            result = None
            exception = None
            try:
                self.bstack11l1l1lll11_opy_(hook_type, self._11l1l1ll1l1_opy_[hook_type], (this, arg))
                result = Result(result=bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫឹ"))
            except Exception as e:
                result = Result(result=bstack11lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬឺ"), exception=e)
                self.handler(hook_type, bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬុ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11lll1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ូ"), result)
        if hook_type in [bstack11lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧួ"), bstack11lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫើ")]:
            return bstack11l1ll11111_opy_
        return bstack11l1l1lll1l_opy_
    def bstack11l1l1ll1ll_opy_(self, bstack11l1l1l1l11_opy_):
        def bstack11l1ll111l1_opy_(this, *args, **kwargs):
            self.bstack11l1l1llll1_opy_(this, bstack11l1l1l1l11_opy_)
            self._11l1ll11l11_opy_[bstack11l1l1l1l11_opy_](this, *args, **kwargs)
        return bstack11l1ll111l1_opy_