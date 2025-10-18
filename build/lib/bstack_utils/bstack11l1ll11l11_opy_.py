# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll111l1_opy_
from browserstack_sdk.bstack1111ll1l_opy_ import bstack11l11ll1_opy_
def _11l1l1lllll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll11l1l_opy_:
    def __init__(self, handler):
        self._11l1ll1111l_opy_ = {}
        self._11l1ll1l111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11l11ll1_opy_.version()
        if bstack11l1ll111l1_opy_(pytest_version, bstack1l1lll1_opy_ (u"ࠦ࠽࠴࠱࠯࠳ࠥᝳ")) >= 0:
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝴")] = Module._register_setup_function_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝵")] = Module._register_setup_module_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝶")] = Class._register_setup_class_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝷")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝸"))
            Module._register_setup_module_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝹"))
            Class._register_setup_class_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝺"))
            Class._register_setup_method_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝻"))
        else:
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝼")] = Module._inject_setup_function_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝽")] = Module._inject_setup_module_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝾")] = Class._inject_setup_class_fixture
            self._11l1ll1111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝿")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ក"))
            Module._inject_setup_module_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬខ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬគ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1lll1l_opy_(bstack1l1lll1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឃ"))
    def bstack11l1ll1l1ll_opy_(self, bstack11l1ll111ll_opy_, hook_type):
        bstack11l1l1llll1_opy_ = id(bstack11l1ll111ll_opy_.__class__)
        if (bstack11l1l1llll1_opy_, hook_type) in self._11l1ll1l111_opy_:
            return
        meth = getattr(bstack11l1ll111ll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll1l111_opy_[(bstack11l1l1llll1_opy_, hook_type)] = meth
            setattr(bstack11l1ll111ll_opy_, hook_type, self.bstack11l1ll1ll11_opy_(hook_type, bstack11l1l1llll1_opy_))
    def bstack11l1ll1l1l1_opy_(self, instance, bstack11l1ll11111_opy_):
        if bstack11l1ll11111_opy_ == bstack1l1lll1_opy_ (u"ࠢࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠥង"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤច"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨឆ"))
        if bstack11l1ll11111_opy_ == bstack1l1lll1_opy_ (u"ࠥࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠦជ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠥឈ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠢញ"))
        if bstack11l1ll11111_opy_ == bstack1l1lll1_opy_ (u"ࠨࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࠨដ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠧឋ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠤឌ"))
        if bstack11l1ll11111_opy_ == bstack1l1lll1_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឍ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠤណ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩࠨត"))
    @staticmethod
    def bstack11l1ll11ll1_opy_(hook_type, func, args):
        if hook_type in [bstack1l1lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫថ"), bstack1l1lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨទ")]:
            _11l1l1lllll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll1ll11_opy_(self, hook_type, bstack11l1l1llll1_opy_):
        def bstack11l1ll11lll_opy_(arg=None):
            self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧធ"))
            result = None
            try:
                bstack1l11111l1ll_opy_ = self._11l1ll1l111_opy_[(bstack11l1l1llll1_opy_, hook_type)]
                self.bstack11l1ll11ll1_opy_(hook_type, bstack1l11111l1ll_opy_, (arg,))
                result = Result(result=bstack1l1lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨន"))
            except Exception as e:
                result = Result(result=bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩប"), exception=e)
                self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩផ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪព"), result)
        def bstack11l1ll1l11l_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬភ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11ll1_opy_(hook_type, self._11l1ll1l111_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1lll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ម"))
            except Exception as e:
                result = Result(result=bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧយ"), exception=e)
                self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧរ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨល"), result)
        if hook_type in [bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩវ"), bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឝ")]:
            return bstack11l1ll1l11l_opy_
        return bstack11l1ll11lll_opy_
    def bstack11l1l1lll1l_opy_(self, bstack11l1ll11111_opy_):
        def bstack11l1ll1ll1l_opy_(this, *args, **kwargs):
            self.bstack11l1ll1l1l1_opy_(this, bstack11l1ll11111_opy_)
            self._11l1ll1111l_opy_[bstack11l1ll11111_opy_](this, *args, **kwargs)
        return bstack11l1ll1ll1l_opy_