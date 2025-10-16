# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll111ll_opy_
from browserstack_sdk.bstack1111lll1_opy_ import bstack1llll1lll_opy_
def _11l1ll1lll1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll1l1l1_opy_:
    def __init__(self, handler):
        self._11l1ll1l11l_opy_ = {}
        self._11l1ll11111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llll1lll_opy_.version()
        if bstack11l1ll111ll_opy_(pytest_version, bstack1lllll1_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣ᝸")) >= 0:
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝹")] = Module._register_setup_function_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝺")] = Module._register_setup_module_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝻")] = Class._register_setup_class_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝼")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝽"))
            Module._register_setup_module_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝾"))
            Class._register_setup_class_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝿"))
            Class._register_setup_method_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫក"))
        else:
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧខ")] = Module._inject_setup_function_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭គ")] = Module._inject_setup_module_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ឃ")] = Class._inject_setup_class_fixture
            self._11l1ll1l11l_opy_[bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨង")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫច"))
            Module._inject_setup_module_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪឆ"))
            Class._inject_setup_class_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪជ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll111l1_opy_(bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឈ"))
    def bstack11l1ll1111l_opy_(self, bstack11l1ll1l111_opy_, hook_type):
        bstack11l1ll1l1ll_opy_ = id(bstack11l1ll1l111_opy_.__class__)
        if (bstack11l1ll1l1ll_opy_, hook_type) in self._11l1ll11111_opy_:
            return
        meth = getattr(bstack11l1ll1l111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll11111_opy_[(bstack11l1ll1l1ll_opy_, hook_type)] = meth
            setattr(bstack11l1ll1l111_opy_, hook_type, self.bstack11l1ll11lll_opy_(hook_type, bstack11l1ll1l1ll_opy_))
    def bstack11l1ll1ll1l_opy_(self, instance, bstack11l1ll1llll_opy_):
        if bstack11l1ll1llll_opy_ == bstack1lllll1_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣញ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢដ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦឋ"))
        if bstack11l1ll1llll_opy_ == bstack1lllll1_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឌ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣឍ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧណ"))
        if bstack11l1ll1llll_opy_ == bstack1lllll1_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦត"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥថ"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢទ"))
        if bstack11l1ll1llll_opy_ == bstack1lllll1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣធ"):
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢន"))
            self.bstack11l1ll1111l_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦប"))
    @staticmethod
    def bstack11l1ll11ll1_opy_(hook_type, func, args):
        if hook_type in [bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩផ"), bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ព")]:
            _11l1ll1lll1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll11lll_opy_(self, hook_type, bstack11l1ll1l1ll_opy_):
        def bstack11l1lll1111_opy_(arg=None):
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬភ"))
            result = None
            try:
                bstack1l11111l1l1_opy_ = self._11l1ll11111_opy_[(bstack11l1ll1l1ll_opy_, hook_type)]
                self.bstack11l1ll11ll1_opy_(hook_type, bstack1l11111l1l1_opy_, (arg,))
                result = Result(result=bstack1lllll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ម"))
            except Exception as e:
                result = Result(result=bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧយ"), exception=e)
                self.handler(hook_type, bstack1lllll1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧរ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨល"), result)
        def bstack11l1ll1ll11_opy_(this, arg=None):
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪវ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11ll1_opy_(hook_type, self._11l1ll11111_opy_[hook_type], (this, arg))
                result = Result(result=bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫឝ"))
            except Exception as e:
                result = Result(result=bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬឞ"), exception=e)
                self.handler(hook_type, bstack1lllll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬស"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ហ"), result)
        if hook_type in [bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧឡ"), bstack1lllll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫអ")]:
            return bstack11l1ll1ll11_opy_
        return bstack11l1lll1111_opy_
    def bstack11l1ll111l1_opy_(self, bstack11l1ll1llll_opy_):
        def bstack11l1ll11l1l_opy_(this, *args, **kwargs):
            self.bstack11l1ll1ll1l_opy_(this, bstack11l1ll1llll_opy_)
            self._11l1ll1l11l_opy_[bstack11l1ll1llll_opy_](this, *args, **kwargs)
        return bstack11l1ll11l1l_opy_