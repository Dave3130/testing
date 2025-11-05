# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l1l11l1_opy_
from browserstack_sdk.bstack1lll1llll_opy_ import bstack1llllll1l_opy_
def _11l1l1l11ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1ll11l_opy_:
    def __init__(self, handler):
        self._11l1l1ll1l1_opy_ = {}
        self._11l1l1l1111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llllll1l_opy_.version()
        if bstack11l1l1l11l1_opy_(pytest_version, bstack11111_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢា")) >= 0:
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬិ")] = Module._register_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫី")] = Module._register_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឹ")] = Class._register_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឺ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩុ"))
            Module._register_setup_module_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨូ"))
            Class._register_setup_class_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨួ"))
            Class._register_setup_method_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪើ"))
        else:
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឿ")] = Module._inject_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬៀ")] = Module._inject_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬេ")] = Class._inject_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧែ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪៃ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩោ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩៅ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1ll111_opy_(bstack11111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫំ"))
    def bstack11l1l11ll11_opy_(self, bstack11l1l1l1lll_opy_, hook_type):
        bstack11l1l1lll11_opy_ = id(bstack11l1l1l1lll_opy_.__class__)
        if (bstack11l1l1lll11_opy_, hook_type) in self._11l1l1l1111_opy_:
            return
        meth = getattr(bstack11l1l1l1lll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1l1111_opy_[(bstack11l1l1lll11_opy_, hook_type)] = meth
            setattr(bstack11l1l1l1lll_opy_, hook_type, self.bstack11l1l11lll1_opy_(hook_type, bstack11l1l1lll11_opy_))
    def bstack11l1l1l1l1l_opy_(self, instance, bstack11l1l11llll_opy_):
        if bstack11l1l11llll_opy_ == bstack11111_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢះ"):
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨៈ"))
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥ៉"))
        if bstack11l1l11llll_opy_ == bstack11111_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣ៊"):
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢ់"))
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦ៌"))
        if bstack11l1l11llll_opy_ == bstack11111_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥ៍"):
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤ៎"))
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨ៏"))
        if bstack11l1l11llll_opy_ == bstack11111_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ័"):
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨ៑"))
            self.bstack11l1l11ll11_opy_(instance.obj, bstack11111_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦ្ࠥ"))
    @staticmethod
    def bstack11l1l1l1l11_opy_(hook_type, func, args):
        if hook_type in [bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨ៓"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬ។")]:
            _11l1l1l11ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l11lll1_opy_(self, hook_type, bstack11l1l1lll11_opy_):
        def bstack11l1l1ll1ll_opy_(arg=None):
            self.handler(hook_type, bstack11111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ៕"))
            result = None
            try:
                bstack11lllll11ll_opy_ = self._11l1l1l1111_opy_[(bstack11l1l1lll11_opy_, hook_type)]
                self.bstack11l1l1l1l11_opy_(hook_type, bstack11lllll11ll_opy_, (arg,))
                result = Result(result=bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ៖"))
            except Exception as e:
                result = Result(result=bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ៗ"), exception=e)
                self.handler(hook_type, bstack11111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭៘"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧ៙"), result)
        def bstack11l1l11ll1l_opy_(this, arg=None):
            self.handler(hook_type, bstack11111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ៚"))
            result = None
            exception = None
            try:
                self.bstack11l1l1l1l11_opy_(hook_type, self._11l1l1l1111_opy_[hook_type], (this, arg))
                result = Result(result=bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ៛"))
            except Exception as e:
                result = Result(result=bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫៜ"), exception=e)
                self.handler(hook_type, bstack11111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ៝"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ៞"), result)
        if hook_type in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭៟"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪ០")]:
            return bstack11l1l11ll1l_opy_
        return bstack11l1l1ll1ll_opy_
    def bstack11l1l1ll111_opy_(self, bstack11l1l11llll_opy_):
        def bstack11l1l1l111l_opy_(this, *args, **kwargs):
            self.bstack11l1l1l1l1l_opy_(this, bstack11l1l11llll_opy_)
            self._11l1l1ll1l1_opy_[bstack11l1l11llll_opy_](this, *args, **kwargs)
        return bstack11l1l1l111l_opy_