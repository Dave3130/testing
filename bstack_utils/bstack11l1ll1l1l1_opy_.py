# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll1ll1l_opy_
from browserstack_sdk.bstack1lll1llll_opy_ import bstack111l11l1_opy_
def _11l1ll111l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll11l1l_opy_:
    def __init__(self, handler):
        self._11l1ll1111l_opy_ = {}
        self._11l1ll1l11l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111l11l1_opy_.version()
        if bstack11l1ll1ll1l_opy_(pytest_version, bstack1ll11_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢ᝷")) >= 0:
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝸")] = Module._register_setup_function_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝹")] = Module._register_setup_module_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝺")] = Class._register_setup_class_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝻")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝼"))
            Module._register_setup_module_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝽"))
            Class._register_setup_class_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝾"))
            Class._register_setup_method_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝿"))
        else:
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ក")] = Module._inject_setup_function_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬខ")] = Module._inject_setup_module_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬគ")] = Class._inject_setup_class_fixture
            self._11l1ll1111l_opy_[bstack1ll11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧឃ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪង"))
            Module._inject_setup_module_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩច"))
            Class._inject_setup_class_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩឆ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll1l111_opy_(bstack1ll11_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫជ"))
    def bstack11l1lll1111_opy_(self, bstack11l1ll1ll11_opy_, hook_type):
        bstack11l1ll111ll_opy_ = id(bstack11l1ll1ll11_opy_.__class__)
        if (bstack11l1ll111ll_opy_, hook_type) in self._11l1ll1l11l_opy_:
            return
        meth = getattr(bstack11l1ll1ll11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll1l11l_opy_[(bstack11l1ll111ll_opy_, hook_type)] = meth
            setattr(bstack11l1ll1ll11_opy_, hook_type, self.bstack11l1ll1llll_opy_(hook_type, bstack11l1ll111ll_opy_))
    def bstack11l1ll11lll_opy_(self, instance, bstack11l1ll11111_opy_):
        if bstack11l1ll11111_opy_ == bstack1ll11_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢឈ"):
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨញ"))
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥដ"))
        if bstack11l1ll11111_opy_ == bstack1ll11_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឋ"):
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢឌ"))
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦឍ"))
        if bstack11l1ll11111_opy_ == bstack1ll11_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥណ"):
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤត"))
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨថ"))
        if bstack11l1ll11111_opy_ == bstack1ll11_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢទ"):
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨធ"))
            self.bstack11l1lll1111_opy_(instance.obj, bstack1ll11_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥន"))
    @staticmethod
    def bstack11l1ll11ll1_opy_(hook_type, func, args):
        if hook_type in [bstack1ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨប"), bstack1ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬផ")]:
            _11l1ll111l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll1llll_opy_(self, hook_type, bstack11l1ll111ll_opy_):
        def bstack11l1ll1lll1_opy_(arg=None):
            self.handler(hook_type, bstack1ll11_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫព"))
            result = None
            try:
                bstack1l11111l1ll_opy_ = self._11l1ll1l11l_opy_[(bstack11l1ll111ll_opy_, hook_type)]
                self.bstack11l1ll11ll1_opy_(hook_type, bstack1l11111l1ll_opy_, (arg,))
                result = Result(result=bstack1ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬភ"))
            except Exception as e:
                result = Result(result=bstack1ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ម"), exception=e)
                self.handler(hook_type, bstack1ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭យ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll11_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧរ"), result)
        def bstack11l1ll1l1ll_opy_(this, arg=None):
            self.handler(hook_type, bstack1ll11_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩល"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11ll1_opy_(hook_type, self._11l1ll1l11l_opy_[hook_type], (this, arg))
                result = Result(result=bstack1ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪវ"))
            except Exception as e:
                result = Result(result=bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫឝ"), exception=e)
                self.handler(hook_type, bstack1ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫឞ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬស"), result)
        if hook_type in [bstack1ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ហ"), bstack1ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪឡ")]:
            return bstack11l1ll1l1ll_opy_
        return bstack11l1ll1lll1_opy_
    def bstack11l1ll1l111_opy_(self, bstack11l1ll11111_opy_):
        def bstack11l1ll11l11_opy_(this, *args, **kwargs):
            self.bstack11l1ll11lll_opy_(this, bstack11l1ll11111_opy_)
            self._11l1ll1111l_opy_[bstack11l1ll11111_opy_](this, *args, **kwargs)
        return bstack11l1ll11l11_opy_