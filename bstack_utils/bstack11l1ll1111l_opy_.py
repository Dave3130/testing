# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l1l1lll_opy_
from browserstack_sdk.bstack111l111l_opy_ import bstack1lll11lll_opy_
def _11l1l1l1ll1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1l1l1l_opy_:
    def __init__(self, handler):
        self._11l1l1ll1ll_opy_ = {}
        self._11l1l1l1l11_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1lll11lll_opy_.version()
        if bstack11l1l1l1lll_opy_(pytest_version, bstack11ll_opy_ (u"ࠥ࠼࠳࠷࠮࠲ࠤវ")) >= 0:
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឝ")] = Module._register_setup_function_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឞ")] = Module._register_setup_module_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ស")] = Class._register_setup_class_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨហ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឡ"))
            Module._register_setup_module_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪអ"))
            Class._register_setup_class_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឣ"))
            Class._register_setup_method_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឤ"))
        else:
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឥ")] = Module._inject_setup_function_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឦ")] = Module._inject_setup_module_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឧ")] = Class._inject_setup_class_fixture
            self._11l1l1ll1ll_opy_[bstack11ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឨ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឩ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឪ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឫ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1lll1l_opy_(bstack11ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឬ"))
    def bstack11l1ll111ll_opy_(self, bstack11l1l1ll1l1_opy_, hook_type):
        bstack11l1l1ll11l_opy_ = id(bstack11l1l1ll1l1_opy_.__class__)
        if (bstack11l1l1ll11l_opy_, hook_type) in self._11l1l1l1l11_opy_:
            return
        meth = getattr(bstack11l1l1ll1l1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1l1l11_opy_[(bstack11l1l1ll11l_opy_, hook_type)] = meth
            setattr(bstack11l1l1ll1l1_opy_, hook_type, self.bstack11l1ll11111_opy_(hook_type, bstack11l1l1ll11l_opy_))
    def bstack11l1l1llll1_opy_(self, instance, bstack11l1l1ll111_opy_):
        if bstack11l1l1ll111_opy_ == bstack11ll_opy_ (u"ࠨࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឭ"):
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣឮ"))
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧឯ"))
        if bstack11l1l1ll111_opy_ == bstack11ll_opy_ (u"ࠤࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឰ"):
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠤឱ"))
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࠨឲ"))
        if bstack11l1l1ll111_opy_ == bstack11ll_opy_ (u"ࠧࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠧឳ"):
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠦ឴"))
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠣ឵"))
        if bstack11l1l1ll111_opy_ == bstack11ll_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠤា"):
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠣិ"))
            self.bstack11l1ll111ll_opy_(instance.obj, bstack11ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠧី"))
    @staticmethod
    def bstack11l1ll11l11_opy_(hook_type, func, args):
        if hook_type in [bstack11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪឹ"), bstack11ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧឺ")]:
            _11l1l1l1ll1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll11111_opy_(self, hook_type, bstack11l1l1ll11l_opy_):
        def bstack11l1l1lll11_opy_(arg=None):
            self.handler(hook_type, bstack11ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ុ"))
            result = None
            try:
                bstack1l1111111l1_opy_ = self._11l1l1l1l11_opy_[(bstack11l1l1ll11l_opy_, hook_type)]
                self.bstack11l1ll11l11_opy_(hook_type, bstack1l1111111l1_opy_, (arg,))
                result = Result(result=bstack11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧូ"))
            except Exception as e:
                result = Result(result=bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨួ"), exception=e)
                self.handler(hook_type, bstack11ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨើ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩឿ"), result)
        def bstack11l1ll111l1_opy_(this, arg=None):
            self.handler(hook_type, bstack11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫៀ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11l11_opy_(hook_type, self._11l1l1l1l11_opy_[hook_type], (this, arg))
                result = Result(result=bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬេ"))
            except Exception as e:
                result = Result(result=bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ែ"), exception=e)
                self.handler(hook_type, bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ៃ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧោ"), result)
        if hook_type in [bstack11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨៅ"), bstack11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬំ")]:
            return bstack11l1ll111l1_opy_
        return bstack11l1l1lll11_opy_
    def bstack11l1l1lll1l_opy_(self, bstack11l1l1ll111_opy_):
        def bstack11l1l1lllll_opy_(this, *args, **kwargs):
            self.bstack11l1l1llll1_opy_(this, bstack11l1l1ll111_opy_)
            self._11l1l1ll1ll_opy_[bstack11l1l1ll111_opy_](this, *args, **kwargs)
        return bstack11l1l1lllll_opy_