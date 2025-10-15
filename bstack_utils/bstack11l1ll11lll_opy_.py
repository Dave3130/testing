# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll1l111_opy_
from browserstack_sdk.bstack1llll111l_opy_ import bstack111l1l11_opy_
def _11l1ll1l1l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll11l11_opy_:
    def __init__(self, handler):
        self._11l1l1lllll_opy_ = {}
        self._11l1ll1lll1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111l1l11_opy_.version()
        if bstack11l1ll1l111_opy_(pytest_version, bstack1ll1l_opy_ (u"ࠥ࠼࠳࠷࠮࠲ࠤᝲ")) >= 0:
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᝳ")] = Module._register_setup_function_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝴")] = Module._register_setup_module_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝵")] = Class._register_setup_class_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝶")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝷"))
            Module._register_setup_module_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝸"))
            Class._register_setup_class_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝹"))
            Class._register_setup_method_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝺"))
        else:
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝻")] = Module._inject_setup_function_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝼")] = Module._inject_setup_module_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝽")] = Class._inject_setup_class_fixture
            self._11l1l1lllll_opy_[bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝾")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝿"))
            Module._inject_setup_module_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫក"))
            Class._inject_setup_class_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫខ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll1111l_opy_(bstack1ll1l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭គ"))
    def bstack11l1ll1l1ll_opy_(self, bstack11l1ll111ll_opy_, hook_type):
        bstack11l1ll11ll1_opy_ = id(bstack11l1ll111ll_opy_.__class__)
        if (bstack11l1ll11ll1_opy_, hook_type) in self._11l1ll1lll1_opy_:
            return
        meth = getattr(bstack11l1ll111ll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll1lll1_opy_[(bstack11l1ll11ll1_opy_, hook_type)] = meth
            setattr(bstack11l1ll111ll_opy_, hook_type, self.bstack11l1l1llll1_opy_(hook_type, bstack11l1ll11ll1_opy_))
    def bstack11l1ll1ll11_opy_(self, instance, bstack11l1ll1ll1l_opy_):
        if bstack11l1ll1ll1l_opy_ == bstack1ll1l_opy_ (u"ࠨࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឃ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣង"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧច"))
        if bstack11l1ll1ll1l_opy_ == bstack1ll1l_opy_ (u"ࠤࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠥឆ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠤជ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࠨឈ"))
        if bstack11l1ll1ll1l_opy_ == bstack1ll1l_opy_ (u"ࠧࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠧញ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠦដ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠣឋ"))
        if bstack11l1ll1ll1l_opy_ == bstack1ll1l_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឌ"):
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠣឍ"))
            self.bstack11l1ll1l1ll_opy_(instance.obj, bstack1ll1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠧណ"))
    @staticmethod
    def bstack11l1ll11111_opy_(hook_type, func, args):
        if hook_type in [bstack1ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪត"), bstack1ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧថ")]:
            _11l1ll1l1l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1llll1_opy_(self, hook_type, bstack11l1ll11ll1_opy_):
        def bstack11l1ll1l11l_opy_(arg=None):
            self.handler(hook_type, bstack1ll1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ទ"))
            result = None
            try:
                bstack1l1111111ll_opy_ = self._11l1ll1lll1_opy_[(bstack11l1ll11ll1_opy_, hook_type)]
                self.bstack11l1ll11111_opy_(hook_type, bstack1l1111111ll_opy_, (arg,))
                result = Result(result=bstack1ll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧធ"))
            except Exception as e:
                result = Result(result=bstack1ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨន"), exception=e)
                self.handler(hook_type, bstack1ll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨប"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩផ"), result)
        def bstack11l1ll11l1l_opy_(this, arg=None):
            self.handler(hook_type, bstack1ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫព"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11111_opy_(hook_type, self._11l1ll1lll1_opy_[hook_type], (this, arg))
                result = Result(result=bstack1ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬភ"))
            except Exception as e:
                result = Result(result=bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ម"), exception=e)
                self.handler(hook_type, bstack1ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭យ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧរ"), result)
        if hook_type in [bstack1ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨល"), bstack1ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬវ")]:
            return bstack11l1ll11l1l_opy_
        return bstack11l1ll1l11l_opy_
    def bstack11l1ll1111l_opy_(self, bstack11l1ll1ll1l_opy_):
        def bstack11l1ll111l1_opy_(this, *args, **kwargs):
            self.bstack11l1ll1ll11_opy_(this, bstack11l1ll1ll1l_opy_)
            self._11l1l1lllll_opy_[bstack11l1ll1ll1l_opy_](this, *args, **kwargs)
        return bstack11l1ll111l1_opy_