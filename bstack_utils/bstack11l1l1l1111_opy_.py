# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1l11llll_opy_
from browserstack_sdk.bstack1lllllll1_opy_ import bstack1lll111l1_opy_
def _11l1l11ll1l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l11ll11_opy_:
    def __init__(self, handler):
        self._11l1l1ll1l1_opy_ = {}
        self._11l1l1l11l1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1lll111l1_opy_.version()
        if bstack11l1l11llll_opy_(pytest_version, bstack11ll1ll_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣិ")) >= 0:
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ី")] = Module._register_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឹ")] = Module._register_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឺ")] = Class._register_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧុ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪូ"))
            Module._register_setup_module_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩួ"))
            Class._register_setup_class_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩើ"))
            Class._register_setup_method_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫឿ"))
        else:
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧៀ")] = Module._inject_setup_function_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭េ")] = Module._inject_setup_module_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ែ")] = Class._inject_setup_class_fixture
            self._11l1l1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨៃ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫោ"))
            Module._inject_setup_module_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪៅ"))
            Class._inject_setup_class_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪំ"))
            Class._inject_setup_method_fixture = self.bstack11l1l1ll1ll_opy_(bstack11ll1ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬះ"))
    def bstack11l1l11lll1_opy_(self, bstack11l1l1l1ll1_opy_, hook_type):
        bstack11l1l1l11ll_opy_ = id(bstack11l1l1l1ll1_opy_.__class__)
        if (bstack11l1l1l11ll_opy_, hook_type) in self._11l1l1l11l1_opy_:
            return
        meth = getattr(bstack11l1l1l1ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1l11l1_opy_[(bstack11l1l1l11ll_opy_, hook_type)] = meth
            setattr(bstack11l1l1l1ll1_opy_, hook_type, self.bstack11l1l1l1lll_opy_(hook_type, bstack11l1l1l11ll_opy_))
    def bstack11l1l1ll111_opy_(self, instance, bstack11l1l1lll11_opy_):
        if bstack11l1l1lll11_opy_ == bstack11ll1ll_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣៈ"):
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢ៉"))
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦ៊"))
        if bstack11l1l1lll11_opy_ == bstack11ll1ll_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤ់"):
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣ៌"))
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧ៍"))
        if bstack11l1l1lll11_opy_ == bstack11ll1ll_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦ៎"):
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥ៏"))
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢ័"))
        if bstack11l1l1lll11_opy_ == bstack11ll1ll_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣ៑"):
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪ្ࠢ"))
            self.bstack11l1l11lll1_opy_(instance.obj, bstack11ll1ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦ៓"))
    @staticmethod
    def bstack11l1l1l1l1l_opy_(hook_type, func, args):
        if hook_type in [bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩ។"), bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭៕")]:
            _11l1l11ll1l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1l1lll_opy_(self, hook_type, bstack11l1l1l11ll_opy_):
        def bstack11l1l1l111l_opy_(arg=None):
            self.handler(hook_type, bstack11ll1ll_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ៖"))
            result = None
            try:
                bstack11llllll1ll_opy_ = self._11l1l1l11l1_opy_[(bstack11l1l1l11ll_opy_, hook_type)]
                self.bstack11l1l1l1l1l_opy_(hook_type, bstack11llllll1ll_opy_, (arg,))
                result = Result(result=bstack11ll1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ៗ"))
            except Exception as e:
                result = Result(result=bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ៘"), exception=e)
                self.handler(hook_type, bstack11ll1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧ៙"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨ៚"), result)
        def bstack11l1l1ll11l_opy_(this, arg=None):
            self.handler(hook_type, bstack11ll1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ៛"))
            result = None
            exception = None
            try:
                self.bstack11l1l1l1l1l_opy_(hook_type, self._11l1l1l11l1_opy_[hook_type], (this, arg))
                result = Result(result=bstack11ll1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫៜ"))
            except Exception as e:
                result = Result(result=bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ៝"), exception=e)
                self.handler(hook_type, bstack11ll1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ៞"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭៟"), result)
        if hook_type in [bstack11ll1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ០"), bstack11ll1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ១")]:
            return bstack11l1l1ll11l_opy_
        return bstack11l1l1l111l_opy_
    def bstack11l1l1ll1ll_opy_(self, bstack11l1l1lll11_opy_):
        def bstack11l1l1l1l11_opy_(this, *args, **kwargs):
            self.bstack11l1l1ll111_opy_(this, bstack11l1l1lll11_opy_)
            self._11l1l1ll1l1_opy_[bstack11l1l1lll11_opy_](this, *args, **kwargs)
        return bstack11l1l1l1l11_opy_