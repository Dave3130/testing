# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l1l1lll_opy_
from browserstack_sdk.bstack11111111_opy_ import bstack111ll11l_opy_
def _11l1ll1111l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1lllll_opy_:
    def __init__(self, handler):
        self._11l1l1lll1l_opy_ = {}
        self._11l1l1lll11_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111ll11l_opy_.version()
        if bstack11l1l1l1lll_opy_(pytest_version, bstack1lllll1l_opy_ (u"ࠨ࠸࠯࠳࠱࠵ࠧម")) >= 0:
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪយ")] = Module._register_setup_function_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩរ")] = Module._register_setup_module_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩល")] = Class._register_setup_class_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫវ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឝ"))
            Module._register_setup_module_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឞ"))
            Class._register_setup_class_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ស"))
            Class._register_setup_method_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨហ"))
        else:
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឡ")] = Module._inject_setup_function_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪអ")] = Module._inject_setup_module_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឣ")] = Class._inject_setup_class_fixture
            self._11l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឤ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨឥ"))
            Module._inject_setup_module_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឦ"))
            Class._inject_setup_class_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឧ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll111ll_opy_(bstack1lllll1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឨ"))
    def bstack11l1ll11l11_opy_(self, bstack11l1ll11111_opy_, hook_type):
        bstack11l1l1ll111_opy_ = id(bstack11l1ll11111_opy_.__class__)
        if (bstack11l1l1ll111_opy_, hook_type) in self._11l1l1lll11_opy_:
            return
        meth = getattr(bstack11l1ll11111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1lll11_opy_[(bstack11l1l1ll111_opy_, hook_type)] = meth
            setattr(bstack11l1ll11111_opy_, hook_type, self.bstack11l1l1l1l1l_opy_(hook_type, bstack11l1l1ll111_opy_))
    def bstack11l1l1ll11l_opy_(self, instance, bstack11l1l1ll1ll_opy_):
        if bstack11l1l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠤࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠧឩ"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦឪ"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣឫ"))
        if bstack11l1l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠧࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࠨឬ"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠧឭ"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠤឮ"))
        if bstack11l1l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠣࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឯ"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠢឰ"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠦឱ"))
        if bstack11l1l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠧឲ"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠦឳ"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack1lllll1l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠣ឴"))
    @staticmethod
    def bstack11l1ll11l1l_opy_(hook_type, func, args):
        if hook_type in [bstack1lllll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭឵"), bstack1lllll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪា")]:
            _11l1ll1111l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1l1l1l_opy_(self, hook_type, bstack11l1l1ll111_opy_):
        def bstack11l1ll111l1_opy_(arg=None):
            self.handler(hook_type, bstack1lllll1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩិ"))
            result = None
            try:
                bstack11llllllll1_opy_ = self._11l1l1lll11_opy_[(bstack11l1l1ll111_opy_, hook_type)]
                self.bstack11l1ll11l1l_opy_(hook_type, bstack11llllllll1_opy_, (arg,))
                result = Result(result=bstack1lllll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪី"))
            except Exception as e:
                result = Result(result=bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫឹ"), exception=e)
                self.handler(hook_type, bstack1lllll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫឺ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬុ"), result)
        def bstack11l1l1ll1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack1lllll1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧូ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11l1l_opy_(hook_type, self._11l1l1lll11_opy_[hook_type], (this, arg))
                result = Result(result=bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨួ"))
            except Exception as e:
                result = Result(result=bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩើ"), exception=e)
                self.handler(hook_type, bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩឿ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪៀ"), result)
        if hook_type in [bstack1lllll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫេ"), bstack1lllll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨែ")]:
            return bstack11l1l1ll1l1_opy_
        return bstack11l1ll111l1_opy_
    def bstack11l1ll111ll_opy_(self, bstack11l1l1ll1ll_opy_):
        def bstack11l1l1llll1_opy_(this, *args, **kwargs):
            self.bstack11l1l1ll11l_opy_(this, bstack11l1l1ll1ll_opy_)
            self._11l1l1lll1l_opy_[bstack11l1l1ll1ll_opy_](this, *args, **kwargs)
        return bstack11l1l1llll1_opy_